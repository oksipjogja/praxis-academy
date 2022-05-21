const express = require('express');
const expressLayouts = require('express-ejs-layouts');

const {
    body,
    validationResult,
    check
} = require('express-validator')
const methodOverride = require('method-override')

const session = require('express-session');
const cookieParser = require('cookie-parser');
const flash = require('connect-flash');

require('./utils/db');
const Contact = require('./model/contact');

const app = express();
const port = 3000;

// setup method override
app.use(methodOverride('_method'));

// setup ejs
app.set('view engine', 'ejs');
app.use(expressLayouts);
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// konfigurasi flash
app.use(cookieParser('secret'));
app.use(
    session({
        cookie: { maxAge: 6000 },
        secret: 'secret',
        resave: true,
        saveUnintialized: true,
    }));
app.use(flash());

//  Halaman Home
app.get('/', (req, res) => {
    const mahasiswa = [{
            nama: 'Kenthir Widodo',
            email: 'kemplung@gmail.com'
        },
        {
            nama: 'Waluyo Pangarep',
            email: 'wapang@gmail.com',
        },
        {
            nama: 'Singgih Winarso',
            email: 'siwin@gmail.com',
        },
    ];
    res.render('index', {
        layout: 'layouts/main-layout',
        nama: 'Bowo',
        mahasiswa,
        title: 'Halaman Home',
    });
    console.log('ini halaman home')
});

// Halaman About
app.get('/about', (req, res) => {
    res.render('about', {
        title: 'Halaman About',
        layout: 'layouts/main-layout',
    });
});

// Halaman Contact
app.get('/contact', async(req, res) => {
    // Contact.find().then((contact) => {
    //     res.send(contact);
    // });

    const contacts = await Contact.find();

    res.render('contact', {
        title: 'Halaman Contact',
        layout: 'layouts/main-layout',
        contacts,
        msg: req.flash('msg'),
    });
});

// halaman form tambah data contact
app.get('/contact/add', (req, res) => {
    res.render('add-contact', {
        title: 'Form Nambah Data Contact',
        layout: 'layouts/main-layout',
    })
});

// proses tambah data contact
app.post('/contact', [
    body('nama').custom(async(value) => {
        const duplikat = await Contact.findOne({ nama: value });
        if (duplikat) {
            throw new Error('Nama contact sudah digunakan!');
        }
        return true;
    }),
    check('email', 'Email tidak valid!').isEmail(),
    check('nohp', 'No HP tidak valid!').isMobilePhone('id-ID'),
], (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {

        res.render('add-contact', {
            title: 'Form Nambah Data Contact',
            layout: 'layouts/main-layout',
            errors: errors.array(),
        });
    } else {
        Contact.insertMany(req.body, (error, result) => {
            // kirimkan flash message
            req.flash('msg', 'Data contact sukses ditambahkan');
            res.redirect('/contact');
        });
    }
});

// proses delete contact
// app.get('/contact/delete/:nama', async(req, res) => {
//     const contact = await Contact.findOne({ nama: req.params.nama });
//     // jika contact tidak ada
//     if (!contact) {
//         res.status(404);
//         res.send('<h1>404</h1>');
//     } else {
//         // res.send('Oye');
//         });
//     }
// })
app.delete('/contact', (req, res) => {
    Contact.deleteOne({ nama: req.body.nama }).then((result) => {
        req.flash('msg', 'Data contact berhasil dihapus');
        res.redirect('/contact');
    });
});

// form ubah data contact
app.get('/contact/edit/:nama', async(req, res) => {
    const contact = await Contact.findOne({ nama: req.params.nama });

    res.render('edit-contact', {
        title: 'Form Ubah Data Contact',
        layout: 'layouts/main-layout',
        contact,
    });
});

// proses ubah data
app.put(
    '/contact', [
        body('nama').custom(async(value, { req }) => {
            const duplikat = await Contact.findOne({ nama: value });
            if (value !== req.body.oldNama && duplikat) {
                throw new Error('Nama contact sudah digunakan!');
            }
            return true;
        }),
        check('email', 'Email tidak valid!').isEmail(),
        check('nohp', 'No HP tidak valid!').isMobilePhone('id-ID'),
    ],
    (req, res) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            res.render('edit-contact', {
                title: 'Form Ubah Data Contact',
                layout: 'layouts/main-layout',
                errors: errors.array(),
                contact: req.body,
            });
        } else {
            Contact.updateOne({ _id: req.body._id }, {
                $set: {
                    nama: req.body.nama,
                    email: req.body.email,
                    nohp: req.body.nohp
                },
            }).then((result) => {
                // kirimkan flash message
                req.flash('msg', 'Data contact berhasil diubah!');
                res.redirect('/contact');
            });
        }
    });


// halaman detail contact
app.get('/contact/:nama', async(req, res) => {
    const contact = await Contact.findOne({ nama: req.params.nama });

    res.render('detail', {
        title: 'Halaman Detail Contact',
        layout: 'layouts/main-layout',
        contact,
    });
});

app.listen(port, () => {
    console.log(`Mongo Contact App | Listening at http://localhost:${port}`);
});

































// install express-- > npm i express @4 .17 .1
// template engine ejs-- > npm i ejs @3 .1 .6
// install express layouts-- > npm i express - ejs - layouts @2 .5 .0