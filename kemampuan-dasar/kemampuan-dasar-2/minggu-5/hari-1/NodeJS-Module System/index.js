//  const fs = require('fs'); // import core module
//  const moment = require('moment');  // import third party module/npm module node_modules
//  const cetakNama = require('./coba');  // import local module
//  const nama = 'Agung Permadi';
//  const cetakNama = (nama) => `Hi, nama saya ${nama}`;
//  console.log(cetakNama(nama));
//  console.log(window);

const coba = require('./coba');
//  console.log(coba);
console.log(
    coba.cetakNama('Donie'),
    coba.PI,
    coba.mahasiswa.cetakMhs(),
    new coba.Orang()
);