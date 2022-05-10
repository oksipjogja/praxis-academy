// core module
// file system
const fs = require('fs');
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
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question('Masukan nama anda: ', (nama) => {
    rl.question('Masukan nomor hp Anda : ', (noHP) => {
        const contact = { nama, noHP };
        const file = fs.readFileSync('data/constacts.json', 'utf8');
        const contacts = JSON.parse(file);

        contacts.push(contact);

        console.log(constacts)

        rl.close();
    })
})