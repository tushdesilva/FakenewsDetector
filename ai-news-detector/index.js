const express = require ('express');
const app = express ();
const {spawn} = require ('child_process');

// const childPython = spawn ('python', ['fake_news_code/hello.py']);

app.use (express.json ());
app.use (express.urlencoded ({extended: false}));
app.use (express.static (__dirname + '/public'));
app.set ('view engine', 'ejs');

app.get ('/', (req, res) => {
  res.render ('index');
});

app.post ('/check-news', (req, res) => {
  console.log (req.body);
  let article = req.body.article;
  let website = req.body.website;
  let keywords = req.body.keywords;
  const pyProg = spawn ('python', [
    'fake_news_code/ml_backend.py',
    article,
    website,
    keywords,
  ]);

  pyProg.stdout.on ('data', data => {
    console.log (`stdout: ${data}`);
    res.render ('result', {data: data});
    // return;
  });

  pyProg.stderr.on ('data', data => {
    console.log ('stderr: ', data.toString ());
    // return res.sendStatus (400);
  });

  pyProg.on ('close', code => {
    console.log ('Child exited with code : ', code);
  });

  //   res.render ('index');
});

app.listen (5000, () => {
  console.log ('Server running on port 5000');
});
