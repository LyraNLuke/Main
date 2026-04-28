const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const dist = path.join(root, 'dist');

function copyFile(src, dest) {
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
}

function copyFolder(src, dest) {
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyFolder(srcPath, destPath);
    } else if (entry.isFile()) {
      copyFile(srcPath, destPath);
    }
  }
}

if (!fs.existsSync(dist)) {
  fs.mkdirSync(dist, { recursive: true });
}

copyFile(path.join(root, 'manifest.json'), path.join(dist, 'manifest.json'));

const publicFolder = path.join(root, 'public');
if (fs.existsSync(publicFolder)) {
  copyFolder(publicFolder, dist);
}

console.log('Copied manifest.json and public assets to dist/');
