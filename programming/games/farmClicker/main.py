import pygame
import sys


# -- Init --
pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Clicker")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)


# -- Game State --
coins = 0
coins_per_click = 1
passive_income = 0      # coins per second
last_tick = pygame.time.get_ticks()  # ms since game started

# -- Farm Field -
# -
field = pygame.Rect(400, 250, 300, 200)


# -- Game Logic --
upgrades = [
    {"name": "Better Tools", "cost": 10, "cpc_bonus": 1, "bought": False},
    {"name": "Fertilizer", "cost": 50, "cpc_bonus": 3, "bought": False},
    {"name": "Irrigation", "cost": 200, "cpc_bonus": 10, "bought": False},
    {"name": "Chicken Coop", "cost": 100, "passive_bonus": 2, "bought": False}
]

def draw_shop(screen, fon, coins, upgrades):
    panel = pygame.Rect(900, 50, 350, 620)
    pygame.draw.rect(screen, (245, 222, 179), panel)
    pygame.draw.rect(screen, (139, 90, 43,), panel, 4)
    
    title = font.render("Shop", True, (0, 0, 0))
    screen.blit(title, (980, 60))
    
    buttons = []
    for i, upg in enumerate(upgrades):
        btn = pygame.Rect(920, 120 + i * 100, 310, 70)
        color = (180, 220, 180) if not upg["bought"] else (200, 200, 200)
        pygame.draw.rect(screen, color, btn, border_radius=8)
        
        name_text = font.render(upg["name"], True, (0, 0, 0))
        cost_text = font.render(
            "Owned" if upg["bought"] else f"Cost: {upg['cost']} coins",
            True, (100, 100, 100)
        )
        screen.blit(name_text, (btn.x + 10, btn.y +10))
        screen.blit(cost_text, (btn.x + 10, btn.y + 40))
        buttons.append(btn)
    
    return buttons
        

# -- Game Loop --
shop_buttons = []

while True:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # mous click on the field
        if event.type == pygame.MOUSEBUTTONDOWN:
            if field.collidepoint(event.pos):
                coins += coins_per_click
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, btn in enumerate(shop_buttons):
                upg = upgrades[i]
                
                if btn.collidepoint(event.pos) and not upg["bought"] and coins >= upg["cost"]:
                    coins -= upg["cost"]
                    if "cpc_bonus" in upg:
                        coins_per_click += upg["cpc_bonus"]
                    if "passive_bonus" in upg:
                        passive_income += upg["passive_bonus"]
                    upg["bought"] = True

    # update
    now = pygame.time.get_ticks()
    if now - last_tick >= 1000:
        coins += passive_income
        last_tick = now

    # Draw
    screen.fill((100, 180, 100)) # green background
    
    # draw the farm field
    pygame.draw.rect(screen, (210, 180, 100), field) 
    pygame.draw.rect(screen, (80, 50, 20), field, 4) 
    label = font.render("click to harvest", True, (0, 0, 0,))
    screen.blit(label, ( field.x + 30, field.y + 80))
    
    # draw coins
    coin_text = font.render(f"Coins: {coins}", True, (255, 215, 0))
    screen.blit(coin_text, (20, 20))
    
    # draw shop
    shop_buttons = draw_shop(screen, font, coins, upgrades)
    
    pygame.display.flip()
    clock.tick(60) # limit to 60 FPS