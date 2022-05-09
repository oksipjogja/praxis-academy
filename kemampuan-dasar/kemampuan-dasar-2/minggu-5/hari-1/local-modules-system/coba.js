// console.log('Hello World');

function cetakNama(nama) {
    return `Halo, nama saya ${nama}`;   // ===> ini contoh function/method
}

const PI = 3.14;  // ===> ini contoh variabel


const mahasiswa = {
    nama : 'Dody Ferdiansyah',
    umur : 20,
    cetakMhs() {
        return `Halo, nama saya ${this.nama} dan saya ${this.umur} tahun.`;
    }

}
class Orang {
    constructor() {
        console.log('Objek orang telah dibuat!!');
    }
}
// console.log(cetakNama('Donie'));
// module.exports.cetakNama = cetakNama;
// module.exports.PI = PI;
// module.exports.mahasiswa = mahasiswa;   // ====> dapat diringkas dengan cara dibwh ini:
// module.exports.Orang = Orang;


// module.exports = {
//     cetakNama : cetakNama,
//     PI : PI,
//     mahasiswa : mahasiswa,
//     Orang : Orang,
// };                                    // ====> dpt diringkas lagi sbb:

module.exports = { cetakNama, PI, mahasiswa, Orang };