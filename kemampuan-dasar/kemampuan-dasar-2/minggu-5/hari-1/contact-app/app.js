// mengambil argument dari command line
const yargs = require('yargs');
const contacts = require('./contacts');

yargs.command({

        command: 'add',
        describe: 'Menambahkan contact baru',
        builder: {
            nama: {
                describe: 'Nama lengkap',
                demandOption: true,
                type: 'string',
            },
            email: {
                describe: 'Email',
                demandOption: false,
                type: 'string',
            },
            noHP: {
                describe: 'No Handphone',
                demandOption: true,
                type: 'string',
            },
        },
        handler(argv) {
            contacts.saveContact(argv.nama, argv.email, argv.noHP);
        },
    })
    .demandCommand();

// menampikan daftar semua nama contact dan no handphone
yargs.command({
    command: 'list',
    describe: 'Menampilkan daftar contact nama dan no handphone',
    handler() {
        contacts.listContact();
    },
});

// menampilkan detail sebuah contact
yargs.command({
    command: 'detail',
    describe: 'Menampilkan detail sebuah contact berdasarkan nama',
    builder: {
        nama: {
            describe: 'Nama lengkap',
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
    describe: 'Menghapus sebuah contact berdasarkan nama',
    builder: {
        nama: {
            describe: 'Nama lengkap',
            demandOption: true,
            type: 'string',
        },
    },
    handler(argv) {
        contacts.removeContact(argv.nama);
    },
});


yargs.parse();












































// console.log(yargs.argv);
// const contact = {
//     nama: argv.nama,
//     email: argv.email,
//     noHP: argv.noHP,
// };
// console.log(contact);
// const yargs = require('yargs/yargs');
// const { hideBin } = require('yargs/helpers');
// const argv = yargs(hideBin(process.argv)).argv;

// if (argv.ships > 3 && argv.distance < 53.5) {
//     console.log('Plunder more riffiwobbles!');
// } else {
//     console.log('Retreat for the xupptumblers!')
// };

// yargs(hideBin(process.argv))
//     .command('serve [port]', 'start the server', (yargs) => {
//         return yargs
//             .positional('port', {
//                 describe: 'port to bind on',
//                 default: 5000
//             })
//     }, (argv) => {
//         if (argv.verbose) console.info(`start server on :${argv.port}`)
//         serve(argv.port)
//     })
//     .option('verbose', {
//         alias: 'v',
//         type: 'boolean',
//         description: 'Run with verbose logging'
//     })
//     .parse()

// const contacts = require('./contacts');

// const main = async() => {
//     const nama = await contacts.tulisPertanyaan('Masukan nama anda: ');
//     const email = await contacts.tulisPertanyaan('Masukan email anda: ');
//     const noHP = await contacts.tulisPertanyaan('Masukan no handphone anda: ');

//     contacts.saveContact(nama, email, noHP);
// };

// const { tulisPertanyaan, saveContact } = require('./contacts');

// const main = async() => {
//     const nama = await tulisPertanyaan('Masukan nama anda: ');
//     const email = await tulisPertanyaan('Masukan email anda: ');
//     const noHP = await tulisPertanyaan('Masukan no handphone anda: ');

//     saveContact(nama, email, noHP);
// }


// main();

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