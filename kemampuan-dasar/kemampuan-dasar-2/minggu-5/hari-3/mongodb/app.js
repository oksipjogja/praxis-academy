const { MongoClient } = require('mongodb');

const uri = 'mongodb://127.0.0.1:27017';
const dbName = 'OKSIPJOGJA';

const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

client.connect((error, client) => {
    if (error) {
        return console.log('Koneksi Gagal');
    }

    // choose database
    const db = client.db(dbName);
    // Mengubah data berdasarkan id
    db.collection('DtlCont').updateOne({
        _id: ObjectID('627f24bae6dc335eeff9c2b0')
    }, {
        $set: { 'alamat': 'jalan rambutan no 15 yogyakarta', 'pekerjaan': 'karyawan' }
    })
});

updatePromise
    .then((result) => {
        console.log(result);
    })
    .catch((error) => {
        console.log(error);
    });
















// menampilkan data berdasarkan kriteria yang ada di collection 'DtlCont'
// console.log(
//     db.collection('DtlCont')
//     .find({ _id: ObjecID('627f24bae6dc335eeff9c2af') })
//     .toArray((error, result) => {
//         console.log(result);
//     })
// );
// console.log(
//     db
//     .collection('DtlCont')
//     .find({ 'pekerjaan': 'PNS' })
//     .toArray((error, result) => {
//         console.log(result);
//     })
// )

// outputnya :
// [
//     {
//       _id: 627f24bae6dc335eeff9c2af,
//       nama: 'Kenthir Widodo',
//       'alamat ': 'jalan senopati no 15 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '3',
//       penghasilan: '5000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b1,
//       nama: 'Bandot Pamuji',
//       'alamat ': 'jalan roesman no 9 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '5',
//       penghasilan: '8000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b6,
//       nama: 'Sumardi Duldani',
//       'alamat ': 'jalan demangan no 21 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '1',
//       penghasilan: '3000000'
//     }
//   ]






































// menampilkan semua data yang ada di collections DtlCont
// console.log(
//     db
//     .collection('DtlCont')
//     .find()
//     .toArray((error, result) => {
//         console.log(result);
//     })
// );

// outputnya :
// [
//     {
//       _id: 627f24bae6dc335eeff9c2af,
//       nama: 'Kenthir Widodo',
//       'alamat ': 'jalan senopati no 15 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '3',
//       penghasilan: '5000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b0,
//       nama: 'Waluyo Pangarep',
//       'alamat ': 'Jalan maespati no 25B yogyakarta',
//       pekerjaan: 'wiraswasta',
//       'jumlah anak': '2',
//       penghasilan: '3000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b1,
//       nama: 'Bandot Pamuji',
//       'alamat ': 'jalan roesman no 9 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '5',
//       penghasilan: '8000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b2,
//       nama: 'Dobol Permadi',
//       'alamat ': 'jalan ibu dahlan no 90 yogyakarta',
//       pekerjaan: 'Seniman',
//       'jumlah anak': '1',
//       penghasilan: '4000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b3,
//       nama: 'Bagus Triatmojo',
//       'alamat ': 'jalan surabaya no 45 yogyakarta',
//       pekerjaan: 'Seniman',
//       'jumlah anak': '2',
//       penghasilan: '9000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b4,
//       nama: 'Djumadi Sumitro',
//       'alamat ': 'jalan solo no 85 yogyakarta',
//       pekerjaan: 'Karyawan',
//       'jumlah anak': '1',
//       penghasilan: '5000000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b5,
//       nama: 'Djulianto Ramadani',
//       'alamat ': 'jalan magelang no 38 yogyakarta',
//       pekerjaan: 'Karyawan',
//       'jumlah anak': '2',
//       penghasilan: '4500000'
//     },
//     {
//       _id: 627f24bae6dc335eeff9c2b6,
//       nama: 'Sumardi Duldani',
//       'alamat ': 'jalan demangan no 21 yogyakarta',
//       pekerjaan: 'PNS',
//       'jumlah anak': '1',
//       penghasilan: '3000000'
//     },
//     {
//       _id: 6280a0e8159a52783168af2f,
//       nama: 'Wahyu Juniawan',
//       alamat: 'Jalan sawit no 13 yogyakarta',
//       pekerjaan: 'karyawan',
//       'jumlah anak': '1',
//       penghasilan: '3000000'
//     },
//     {
//       _id: 6280afa220eb768336a0d20c,
//       nama: 'Waluyo Sugandi',
//       alamat: 'Jalan rambutan no 23 yogyakarta',
//       pekerjaan: 'karyawan',
//       'jumlah anak': '2',
//       penghasilan: '5000000'
//     },
//     {
//       _id: 6280afa220eb768336a0d20d,
//       nama: 'Subarjo Prawiro',
//       alamat: 'Jalan mangga no 46 yogyakarta',
//       pekerjaan: 'karyawan',
//       'jumlah anak': '0',
//       penghasilan: '2000000'
//     }
//   ]
// Menambahkan 1 data ke collection DtlCont
//     db.collection('DtlCont').insertOne({
//             'nama': 'Wahyu Juniawan',
//             'alamat': 'Jalan sawit no 13 yogyakarta',
//             'pekerjaan': 'karyawan',
//             'jumlah anak': '1',
//             'penghasilan': '3000000'
//         },
//         (error, result) => {
//             if (error) {
//                 return console.log('gagal menambahkan data!');
//             }
//             console.log(result);
//         }
//     );
// });

// menambahkan data lebih dari 1 data
//     db.collection('DtlCont').insertMany(
//         [{
//                 'nama': 'Waluyo Sugandi',
//                 'alamat': 'Jalan rambutan no 23 yogyakarta',
//                 'pekerjaan': 'karyawan',
//                 'jumlah anak': '2',
//                 'penghasilan': '5000000'
//             },
//             {
//                 'nama': 'Subarjo Prawiro',
//                 'alamat': 'Jalan mangga no 46 yogyakarta',
//                 'pekerjaan': 'karyawan',
//                 'jumlah anak': '0',
//                 'penghasilan': '2000000'

//             },

//             (error, result) => {
//                 if (error) {
//                     return console.log('gagal menambahkan data!');
//                 }
//                 console.log(result);
//             }
//         ]
//     );
// });
// console.log('Koneksi Berhasil!');