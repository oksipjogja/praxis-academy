const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/kampus', {
    userNewUrlParser: true,
    useUnifieldTopology: true,
    useCreateIndex: true,
});


// menambah 1 data

// const contact1 = new Contact({
//     nama: 'Wahyudi Prawiro',
//     nohp: '085673188230',
//     email: 'wahpra@gmail.com',
// });

// simpan ke collection
// contact1.save().then((contact) => console.log(contact));