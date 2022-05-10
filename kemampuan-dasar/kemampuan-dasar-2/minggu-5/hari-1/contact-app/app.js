const fs = require('fs');

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const dirPath = './data';
if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath);
}

// membuat file contacts.json jika belum ada
const dataPath = './data/contacts.json';
if (!fs.existsSync(dataPath)) {
    fs.writeFileSync(dataPath, '[]', )
}

const tulisPertanyaan = (pertanyaan) => {
    return new Promise((resolve, reject) => {
        rl.question(pertanyaan, (nama, email, noHP) => {
            resolve(nama, email, noHP);
        });
    });
};

const main = async() => {
    const nama = await tulisPertanyaan('Masukan nama anda: ');
    const email = await tulisPertanyaan('Masukan email anda: ');
    const noHP = await tulisPertanyaan('Masukan no handphone anda: ');
    const contact = { nama, email, noHP };
    const fileBuffer = fs.readFileSync('data/contacts.json', 'utf8');
    const contacts = JSON.parse(fileBuffer);

    contacts.push(contact);

    fs.writeFileSync('data/contacts.json', JSON.stringify(contacts));
    console.log('Matur nuwun sanget melu program niki')
    rl.close();
};

main();





























// const pertanyaan1 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukan nama anda: ', (nama) => {
//             resolve(nama);
//         });
//     });
// };

// const pertanyaan2 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukan email anda: ', (email) => {
//             resolve(email);
//         });
//     });
// };

// const pertanyaan3 = () => {
//     return new Promise((resolve, reject) => {
//         rl.question('Masukan no hp anda: ', (noHP) => {
//             resolve(noHP);
//         });
//     });
// };

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