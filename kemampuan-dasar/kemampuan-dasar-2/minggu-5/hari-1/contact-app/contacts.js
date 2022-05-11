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

const loadContact = () => {
    const fileBuffer = fs.readFileSync('data/contacts.json', 'utf8');
    const contacts = JSON.parse(fileBuffer);
    return contacts;
}

const saveContact = (nama, email, noHP) => {
    const contact = { nama, email, noHP };
    const constacts = loadContact();


    // cek validator emailTornado
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

const listContact = () => {
    const contacts = loadContact();
    console.log(
        chalk.cyan.inverse.bold('Tampilan Data Contact Nama & No HP')
    );
    contacts.forEach((contact, i) => {
        console.log(`${i + 1}. ${contact.nama} - ${contact.noHP}`);
    });
};

const detailContact = (nama) => {
    const contacts = loadContact();

    const contact = contacts.find(
        (contact) => contact.nama.toLowerCase() === nama.toLowerCase()
    );
    if (!contact) {
        console.log(
            chalk.red.inverse.bold(`${nama} tidak ditemukan`));
        return false;
    }
    console.log(chalk.cyan.inverse.bold(contact.nama));
    console.log(contact.noHP);
    if (contact.email) {
        console.log(contact.email);
    }
};

const removeContact = (nama) => {
    const contacts = loadContact();
    const newContacts = contacts.filter(
        (contact) => contact.nama.toLowerCase() !== nama.toLowerCase()
    );
    if (contacts.length === newContacts.length) {
        console.log(
            chalk.red.inverse.bold(`${nama} tidak ditemukan`));
        return false;
    }

    fs.writeFileSync('data/contacts.json', JSON.stringify(newContacts));
    console.log(
        chalk.blue.inverse.bold(`data contact ${nama} berhasil dihapus`)
    );
};

module.exports = { removeContact, detailContact, listContact, saveContact };



















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