
// const nama = 'Donie';
// const fs = require('fs'); // core module
// const cetakNama = require('./coba'); // local modul
// const moment = require('moment'); // third party module / npm module / node_modules
// *** Karena function sebaris tidak usah pake kurung kurawal ***
// const cetakNama = (nama) => {
    //  return `Hi, nama saya ${nama}`;
    // }                     
    // const cetakNama = (nama) => `Hi, nama saya ${nama}`;
    // console.log(cetakNama('Donie Umbara'));
    // console.log(cetakNama(nama));  // menggunakan variabel nama disini berbeda dengan yang di cetakNama itu arg (argumen)
    // console.log(window); ====> error
     // bila '../*' ==> file berada di direktori

// require('./coba');  

// console.log('Hello WPU ');
const coba = require('./coba');
// console.log(coba);      // menunjukan kalau coba object
// console.log(coba.cetakNama('Donie'),coba.PI, coba.mahasiswa.cetakMhs(), new coba.Orang()); // bila tidak ada console.log maka tdk tercetak
console.log(
    coba.cetakNama('Donie'),
    coba.PI,
    coba.mahasiswa.cetakMhs(),
    new coba.Orang()
);