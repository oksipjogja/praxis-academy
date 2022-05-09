const { describe } = require('yargs');
const yargs = require('yargs');
// const { simpanContact } = require('./contacts');  // ===> destructuring langsung
const contacts = require('./contacts');

// membuat parameter object
yargs.command({
    command: 'add',
    describe:  'Menambahkan contact baru',
    builder: {
        nama: {
            describe: "Nama lengkap",
            demandOption: true,
            type: 'string',
        },
        email: {
            describe: 'Email',
            demandOption: true,
            type: 'string',
        },
        noHP: {
            describe: 'No Handphone',
            demandOption: true,
            type: 'string',
        },
    },
    handler(argv) {
        contacts.simpanContact(argv.nama, argv.email, argv.noHP);
    },
}).demandCommand(); 

// menampilkan daftar semua nama contact dan no contact
yargs.command({
    command: 'list',
    describe:  'Menampilkan semua nama, email & no Handphone contact',
    handler() {
        contacts.listContact();
    },
});

// menampilkan detail sebuah contact
yargs.command({
    command: 'detail',
    describe:  'Menampilkan detail sebuah contact berdasarkan nama',
    builder: {
        nama: {
            describe: "Nama lengkap",
            demandOption: true,
            type: 'string',
        },
    },
    handler(argv) {
        contacts.detailContact(argv.nama);
    },
});


// menghapus contact berdasarkan nama
yargs.command({
    command: 'remove',
    describe:  'Menghapus kontak berdasarkan nama',
    builder: {
        nama: {
            describe: "Nama lengkap",
            demandOption: true,
            type: 'string',
        },
    },
    handler(argv) {
        contacts.removeContact(argv.nama);
    },
});


yargs.parse();










