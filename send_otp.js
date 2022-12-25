const { spawn } = require('child_process');

const python = spawn('python', ['path/to/totp.py']);

// Send the secret and method name to the Python script
python.stdin.write(JSON.stringify({ secret: 'abcdefg', method: 'generate' }));
python.stdin.end();

python.stdout.on('data', (data) => {
  console.log(`OTP: ${data}`);
});

python.stderr.on('data', (data) => {
  console.error(`stderr: ${data}`);
});

python.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});
