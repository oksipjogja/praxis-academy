const chalk = require('chalk');

// const validator = require('validator');
// const email = validator.isNumeric('081234456a', 'id=ID');
// console.log(email);
const nama = 'Donie';
// console.log(chalk.bgBlue.bold.red('Hello World'));
const pesan = chalk `Lorem, ipsum dolor {bgBlue.bold.black sit amet} consectetur adipisicing elit. Nama saya : ${nama}`;
console.log(pesan)