// install express-- > npm i express @4 .17 .1
// template engine ejs-- > npm i ejs @3 .1 .6
// install express layouts-- > npm i express - ejs - layouts @2 .5 .0
const express = require('express');
const expressLayouts = require('express-ejs-layouts');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const flash = require('connect-flash');

require('./utils/db');
const Contact = require('./model/contact');

const app = express();
const port = 3000;

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

// halaman detail contact
app.get('/contact/:nama', async(req, res) => {
    const contact = await Contact.findOne({ nama: req.params.nama });

    res.render('detail', {
        title: 'Pelataran Detail Contact',
        layout: 'layouts/main-layout',
        contact,
    });
});

app.listen(port, () => {
    console.log(`Mongo Contact App | Listening at hhtp://localhost:${port}`);
});