const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const { loadContact, findContact } = require('./utils/contacts');

const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.use(expressLayouts); // third-party middleware
app.use(express.static('public'));

app.get('/', (req, res) => {
    const mahasiswa = [{
            nama: 'Kenthir Widodo',
            email: 'kemplung@gmail.com'
        },
        {
            nama: 'Waluyo Pangarep',
            email: 'wapang@gmail.com',
        },
        {
            nama: 'Gendhis Mularti',
            email: 'gemul@gmail.com',
        },
    ];
    res.render('index', {
        nama: 'Bowo',
        title: 'Pelataran Home',
        mahasiswa,
        layout: 'layouts/main-layout',
    });
});

app.get('/about', (req, res) => {
    res.render('about', {
        layout: 'layouts/main-layout',
        title: 'Pelataran About'
    });
});

app.get('/contact', (req, res) => {
    const contacts = loadContact();

    res.render('contact', {
        title: 'Pelataran Contact',
        layout: 'layouts/main-layout',
        contacts,
    });
});

app.get('/about', (req, res) => {
    res.render('about', {
        layout: 'layouts/main-layout',
        title: 'Pelataran About'
    });
});

//detail
app.get('/contact/:nama', (req, res) => {
    const contact = findContact(req.params.nama);

    res.render('detail', {
        title: 'Pelataran Detail Contact',
        layout: 'layouts/main-layout',
        contact,
    });
});

app.use('/', (req, res) => {
    res.status(404);
    res.send('<h1>404</h1>');
});

app.listen(port, () => {

    console.log(`Example app listening at http://localhost:${port}`)
});

































// app.get('/product/:id', (req, res) => {
//     res.send(
//         `Product ID :  ${req.params.id} <br> Category : ${req.query.category}`
//         );
//     });
// Aplication Level Middleware
// app.use((req, res, next) => {
//     console.log('Time :', Date.now());
//     next();
// });
// app.use((req, res, next) => {
//     console.log('ini middleware ke-2');
//     next();
// });
// const morgan = require('morgan');
//gunakan ejs
// app.use(morgan('dev'));
//Built in middleware
// res.sendFile('./index.html', { root: __dirname });
// res.sendFile('./about.html', { root: __dirname });
// res.sendFile('./contact.html', { root: __dirname });
// res.send('<h1>Hello World!</h1>')
// res.json({
//     nama: 'Donie',
//     email: 'donie@gmail.com',
//     noHP: '085869784059',
// });
//  const http = require('http');
// res.send('Menika Pelataran About')
// res.send('Menika Pelataran Contact Bro!!')
//  const fs = require('fs');

//  const port = 3000;

//  const renderHTML = (path, res) => {
//      fs.readFile(path, (err, data) => {
//          if (err) {
//              res.writeHead(404);
//              res.write('Error: file not found');
//          } else {
//              res.write(data);
//          }
//          res.end();
//      });
//  };

//  http
//      .createServer((req, res) => {
//          res.writeHead(200, {
//              'Content-Type': 'text/html'
//          });

//          const url = req.url;
//          // using switch
//          switch (url) {
//              case '/about':
//                  renderHTML('./about.html', res);
//                  break;
//              case '/contact':
//                  renderHTML('./contact.html', res);
//                  break;
//              default:
//                  renderHTML('./index.html', res);
//                  break;
//          }
//      })
//      .listen(port, () => {
//          console.log(`Server is listening on ${port}..`);
//      });
// if (url === '/about') {
//     renderHTML('./about.html', res);
// } else if (url === '/contact') {
//     renderHTML('./contact.html', res);
// } else {
//     renderHTML('./index.html', res);
// }
// res.write('Hello World!');
// console.log(url);
// core module
// file system
// const fs = require('fs');
// menuliskan string ke file(synchronous)
// try {
//     fs.writeFileSync('data/test.txt', 'Hello World secara synchronous');
// } catch (err) {
//     console.log(err);
// }
// menuliskan string ke file(asynchrous)
// fs.writeFile('data/test.txt', 'Hello World secara asynchronous', (err) => {
//     console.log(err);
// });
// membaca isi file (synchronous)
// const data = fs.readFileSync('data/test.txt', 'utf8');
// console.log(data);
// membaca isi file (asynchronous)
// const data = fs.readFile('data/test.txt', 'utf-8', (err, data) => {
//     if (err) throw err;
//     console.log(data);
// });
// Readline
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });
// rl.question('Masukan nama anda: ', (nama) => {
//     rl.question('Masukan nomor hp Anda : ', (noHP) => {
//         const contact = { nama, noHP };
//         const fileBuffer = fs.readFileSync('data/contacts.json', 'utf8');
//         const contacts = JSON.parse(fileBuffer);

//         contacts.push(contact);

//         fs.writeFileSync('data/contacts.json', JSON.stringify(contacts));
//         console.log('Matur nuwun sanget melu program niki')
//         rl.close();
//     });
// });