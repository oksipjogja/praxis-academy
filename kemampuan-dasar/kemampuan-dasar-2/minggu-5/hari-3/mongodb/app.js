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
    const updatePromise = db.collection('contact')
        .updateOne({
            "_id": "627e079d90bbf03d74da9b33"
        }, {
            $set: {
                // 'alamat': 'jalan rambutan no 15 yogyakarta',
                "nama": "Yulianto Ramadani"
            },
        });

    updatePromise
        .then((result) => {
            console.log(result);
        })
        .catch((error) => {
            console.log(error);
        });

    // menghapus 1 date
    // db.collection('contact')
    //     .deleteOne({
    //         "_id": "627e079d90bbf03d74da9b34"
    //     })
    //     .then((result) => {
    //         console.log(result);
    //     })
    //     .catch((error) => {
    //         console.log(error);
    //     });
});







// menampilkan semua data yang ada di collections DtlCont
// console.log(
//     db
//     .collection('DtlCont')
//     .find()
//     .toArray((error, result) => {
//         console.log(result);
//     })
// );

// menampilkan data berdasarkan kriteria yang ada di collection 'DtlCont'
// console.log(
//     db
//     .collection('DtlCont')
//     .find({ 'pekerjaan': 'PNS' })
//     .toArray((error, result) => {
//         console.log(result);
//     })
// )
// console.log(
//     db
//     .collection('contact')
//     .find({ "_id": "627dd85d842b87a01c399688" })
//     .toArray((error, result) => {
//         console.log(result);
//     })
// );

// Menambahkan 1 data ke collection DtlCont
// db.collection('DtlCont').insertOne({
//     'nama': 'Wahyu Juniawan',
//     'alamat': 'Jalan sawit no 13 yogyakarta',
//     'pekerjaan': 'karyawan',
//     'jumlah anak': '1',
//     'penghasilan': '3000000'
// },
// (error, result) => {
//     if (error) {
//         return console.log('gagal menambahkan data!');
//     }
//     console.log(result);
// }
// );

// menambahkan data lebih dari 1 data
// db.collection('DtlCont').insertMany(
// [{
//         'nama': 'Waluyo Sugandi',
//         'alamat': 'Jalan rambutan no 23 yogyakarta',
//         'pekerjaan': 'karyawan',
//         'jumlah anak': '2',
//         'penghasilan': '5000000'
//     },
//     {
//         'nama': 'Subarjo Prawiro',
//         'alamat': 'Jalan mangga no 46 yogyakarta',
//         'pekerjaan': 'karyawan',
//         'jumlah anak': '0',
//         'penghasilan': '2000000'

//     },

//     (error, result) => {
//         if (error) {
//             return console.log('gagal menambahkan data!');
//         }
//         console.log(result);
//     }
// ]
// );
// });
// console.log('Koneksi Berhasil!');