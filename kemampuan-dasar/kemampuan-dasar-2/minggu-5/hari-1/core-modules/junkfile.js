// Core Module
// File Systemnode
// console.log(fs);


// ** menuliskan string ke file (synchronous) **
// try {
//     fs.writeFileSync('data/test.txt', 'Hello World secara synchronous!');
// } catch(e) {
//   console.log(e);
// }


// ** menuliskan string ke file (asynchronous) **
// fs.writeFile('data/test.txt', 'Hello World secara Asynchronous', (e) => {
//     console.log(e);
// })

// ** membaca isi file synchronous **
// const data = fs.readFileSync('data/test.txt', 'utf-8');
// console.log(data);


// ** membaca isi file asynchronous **
// fs.readFile('data/test.txt', 'utf-8', (err, data) => {
//     if (err) throw err;
//     console.log(data);
// });
// Readline 


// membuat folder data jika belum ada


// membuat file contacts.json jika belum ada


// const pertanyaan1 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukkan nama anda : ', (nama) => {
//             resolve(nama);
//         });
//     });
// };

// const pertanyaan2 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukkan email anda : ', (email) => {
//             resolve(email);
//         });
//     });
// };

// const pertanyaan3 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukkan noHP anda : ', (noHP) => {
//             resolve(noHP);
//         });
//     });
// };
// rl.question('Masukkan nama anda : ', (nama) => {
//     rl.question('Masukan nomor HP anda : ', (noHP) => {
//         const contact = { nama, noHP };
//         const file = fs.readFileSync('data/contacts.json', 'utf-8');
//         const contacts = JSON.parse(file);

//         contacts.push(contact);
//         fs.writeFileSync('data/contacts.json', JSON.stringify(contacts));
//         // console.log(contacts);
//         console.log('Terimakasih sudah memasukkan data.');

//         rl.close();
//     });
// });

// const contact = { nama, email, noHP };
//     const fileBuffer = fs.readFileSync('data/contacts.json', 'utf-8');
//         const contacts = JSON.parse(fileBuffer);

//         contacts.push(contact);
//         fs.writeFileSync('data/contacts.json', JSON.stringify(contacts));
//         // console.log(contacts);
//         console.log('Terimakasih sudah memasukkan data.');

//         rl.close();
// outputnya
// Windows@DESKTOP-JN9OIM9 MINGW64 ~/Desktop/belajar-nodejs/core-modules
// $ node app
// Masukkan nama anda : donie
// Masukan nomor HP anda : 0854448880990
// Terimakasih donie, sudah menginputkan 0854448880990

// const contacts = require('./contacts');

// const main = async () => {
//     const nama = await contacts.tulisPertanyaan('Masukan nama anda : ');
//     const email = await contacts.tulisPertanyaan('Masukan email anda : ');
//     const noHP = await contacts.tulisPertanyaan('Masukan noHp anda : ');

//     contacts.simpanContact(nama, email, noHP);
// };

// main();

// membuat parameter satuan
// yargs.command(
//     'add', 
//     'Menambahkan contact baru', 
//     () => {}, 
//     (argv) => {
//         console.log(argv.nama);
//     }
// );
    // handler(argv){
        // const contact = {
        //     nama: argv.nama,
        //     email: argv.email,
        //     noHP: argv.noHP,
        // };
        // console.log(contact);
    //},
// yargs.parse();