const fs = require('fs');

const html = fs.readFileSync('presentation/index.html', 'utf-8');

// Check slide tags
const slideMatches = html.match(/<section\b[^>]*class=["'][^"']*slide[^"']*["']/g) || [];
console.log('Total slide sections in HTML:', slideMatches.length);

// Extract all scripts
const scriptRegex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let scriptContent = '';
while ((match = scriptRegex.exec(html)) !== null) {
  scriptContent += '\n' + match[1];
}

console.log('Extracted scripts length:', scriptContent.length);

// Test syntax of scripts
try {
  new Function(scriptContent);
  console.log('Script syntax: VALID JavaScript');
} catch (e) {
  // Note: some browser APIs like document/window might throw ReferenceError in pure Node, which is normal unless syntax error
  if (e instanceof SyntaxError) {
    console.error('SYNTAX ERROR in presentation script:', e.message);
  } else {
    console.log('Syntax parsed cleanly (expected runtime environment error: ' + e.message + ')');
  }
}

// Check SLIDE_REFS definition
const refsMatch = scriptContent.match(/const\s+SLIDE_REFS\s*=\s*\{([\s\S]*?)\n\};/);
if (refsMatch) {
  const keys = [];
  const keyRegex = /^\s*(\d+):\s*\{/gm;
  let km;
  while ((km = keyRegex.exec(refsMatch[1])) !== null) {
    keys.push(parseInt(km[1], 10));
  }
  console.log('SLIDE_REFS keys count:', keys.length, 'Keys:', keys);
} else {
  console.log('Could not match SLIDE_REFS block in script');
}

// Check N definition
const nMatch = scriptContent.match(/const\s+N\s*=\s*(\d+);/);
console.log('const N in script:', nMatch ? nMatch[1] : 'Not found');
