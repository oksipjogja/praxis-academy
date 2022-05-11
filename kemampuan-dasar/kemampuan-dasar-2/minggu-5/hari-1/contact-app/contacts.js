const fs = require('fs');
const chalk = require('chalk');
const validator = require('validator');

const dirPath = './data';
if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath);
}

// membuat file contacts.json jika belum ada
const dataPath = './data/contacts.json';
if (!fs.existsSync(dataPath)) {
    fs.writeFileSync(dataPath, '[]', 'utf-8');
}

const saveContact = (nama, email, noHP) => {
    const contact = { nama, email, noHP };
    const fileBuffer = fs.readFileSync('data/contacts.json', 'utf8');
    const contacts = JSON.parse(fileBuffer);

    // cek validator email
    if (email) {
        if (!validator.isEmail(email)) {
            console.log(
                chalk.red.inverse.bold('Email tidak valid!!')
            );
            return false;
        }
    }

    // cek validator nomor Handphone
    if (email) {
        if (!validator.isMobilePhone(noHP, 'id-ID')) {
            console.log(
                chalk.red.inverse.bold('No handphone tidak valid!!')
            );
            return false;
        }
    }

    // cek duplikat nomor handphone
    const duplikat = contacts.find((contact) => contact.noHP === noHP);
    if (duplikat) {
        console.log(
            chalk.blue.inverse.bold('No handphone contact sudah terdaftar, ganti nama yang lain!!')
        );
        return false;
    }

    contacts.push(contact);

    fs.writeFileSync('data/contacts.json', JSON.stringify(contacts));
    console.log(
        chalk.blue.inverse.bold('Matur nuwun sanget melu program niki')
    );
};

module.exports = { saveContact };



















// // cek duplikat nama
// const duplikat = contacts.find((contact) => contact.nama === nama);
// if (duplikat) {
//     console.log(
//         chalk.green.inverse.bold('Nama Contact sudah terdaftar, ganti nama yang lain!!')
//     );
//     return false;
// }
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });
// const tulisPertanyaan = (pertanyaan) => {
//     return new Promise((resolve, reject) => {
//         rl.question(pertanyaan, (nama, email, noHP) => {
//             resolve(nama, email, noHP);
//         });
//     });
// };