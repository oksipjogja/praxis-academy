const http = require('http');
const fs = require('fs');

const port = 3000;

const renderHTML = (path, res) => {
    fs.readFile(path, (err, data) => {
        if (err) {
            res.writeHead(404);
            res.write('Error: file not found');
        } else {
            res.write(data);
        }
        res.end();
    });
};

http
    .createServer((req, res) => {
        res.writeHead(200, {
            'Content-Type': 'text/html'
        });

        const url = req.url;
        // using switch
        switch (url) {
            case '/about':
                renderHTML('./about.html', res);
                break;
            case '/contact':
                renderHTML('./contact.html', res);
                break;
            default:
                renderHTML('./index.html', res);
                break;
        }
    })
    .listen(port, () => {
        console.log(`Server is listening on ${port}..`);
    });


































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