const validator = require('validator');
const chalk = require('chalk')
// console.log(validator.isEmail('familybuah@gmail.com'));   // ===> true
// // console.log(validator.isEmail('familybuahgmail.com'));  // ===> false
// console.log(validator.isMobilePhone('085869784059', 'id-ID'));
// console.log(validator.isNumeric('085869784059'));

// console.log(chalk.black.bgBlue('Hello World'));
// console.log(chalk.hex('#DEADED').underline('Hello World'))   // outputnya Hello World underline
// console.log(chalk.rgb(15,100, 204).inverse('Hello!'));
// console.log(chalk.bgHex('#DEADED').underline('Hello, World!'));
// console.log(chalk.bgBlack.white('Hello, World!'));

// const message = 'Selamat Pagi';
// console.log(chalk.bgRed.black(message));

// console.log(`
// CPU: ${chalk.red('90%')}
// RAM: ${chalk.green('40%')}
// DISK: ${chalk.yellow('70%')}
// `);


// const error = chalk.bold.red;
// const warning = chalk.hex('#FFA500'); // orange color

// console.log(error('Error!'));
// console.log(warning('Warning!'));

// const name = "Donie";
// console.log(chalk.green('Hi %s'), name);

const nama = 'Donie';
const pesan = chalk`lorem, {bgBlue white.bold ipsum dolor} {bgRed sit amet} consectetur {bgGreen.italic.black adipisicing} elit. {bgRed.black Nama saya : ${nama}}`;
console.log(pesan);