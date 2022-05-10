// const contacts = require('./contacts');

// const main = async() => {
//     const nama = await contacts.tulisPertanyaan('Masukan nama anda: ');
//     const email = await contacts.tulisPertanyaan('Masukan email anda: ');
//     const noHP = await contacts.tulisPertanyaan('Masukan no handphone anda: ');

//     contacts.saveContact(nama, email, noHP);
// };

const { tulisPertanyaan, saveContact } = require('./contacts');

const main = async() => {
    const nama = await tulisPertanyaan('Masukan nama anda: ');
    const email = await tulisPertanyaan('Masukan email anda: ');
    const noHP = await tulisPertanyaan('Masukan no handphone anda: ');

    saveContact(nama, email, noHP);
}


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