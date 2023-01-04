// 31 - Dec - 2022

import fs from 'fs';

const fileNameRead = fs.readdirSync('.');

let outPut = '';
const jpg = '.jpg';
const png = '.png';

const fileNameContainer = new Set();

// Sort the file names from largest to smallest
const sortedFileNames = fileNameRead
  .filter((file) => file.includes(jpg) || file.includes(png))
  .sort((a, b) => b.length - a.length);

for (const file of sortedFileNames) {
  if (file.includes(jpg)) {
    const jpgFile = file.replace(jpg, '').replace('-', '');
    fileNameContainer.add(jpgFile);
    outPut += `import ${jpgFile} from './${file}';\n`;
  } else if (file.includes(png)) {
    const pngFile = file.replace(png, '').replace('-', '');
    fileNameContainer.add(pngFile);
    outPut += `import ${pngFile} from './${file}';\n`;
  }
}

if (fileNameContainer.size > 0) {
  outPut += '\nconst index = {\n';
  for (const fileName of fileNameContainer) {
    outPut += `\t${fileName},\n`;
  }
  outPut += '}\n\nexport default index;';
}

fs.writeFile("index.js", outPut, (err) => {
  if (err) throw err;
  console.log("✅ [index.js] file has been created successfully!");
});
