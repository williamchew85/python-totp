const express = require('express');
const { spawn } = require('child_process');

const app = express();

app.use(express.json());

app.post('/send-email', (req, res) => {
  const { email } = req.body;

  const python = spawn('python', ['path/to/totp.py']);

  // Send the email to the Python script
  python.stdin.write(JSON.stringify({ email }));
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

  res.send({ message: 'Email sent!' });
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
