const fs = require('fs');

// console.log(fs);
// outputnya menunjukan dict fs :
// Windows@DESKTOP-JN9OIM9 MINGW64 ~/Desktop/belajar-nodejs/core-modules
// $ node app
// {
//   appendFile: [Function: appendFile],
//   appendFileSync: [Function: appendFileSync],
//   access: [Function: access],
//   accessSync: [Function: accessSync],
//   chown: [Function: chown],
//   chownSync: [Function: chownSync],
//   chmod: [Function: chmod],
//   chmodSync: [Function: chmodSync],
//   close: [Function: close],
//   closeSync: [Function: closeSync],
//   copyFile: [Function: copyFile],
//   copyFileSync: [Function: copyFileSync],
//   cp: [Function: cp],
//   cpSync: [Function: cpSync],
//   createReadStream: [Function: createReadStream],
//   createWriteStream: [Function: createWriteStream],
//   exists: [Function: exists],
//   existsSync: [Function: existsSync],
//   fchown: [Function: fchown],
//   fchownSync: [Function: fchownSync],
//   fchmod: [Function: fchmod],
//   fchmodSync: [Function: fchmodSync],
//   fdatasync: [Function: fdatasync],
//   fdatasyncSync: [Function: fdatasyncSync],
//   fstat: [Function: fstat],
//   fstatSync: [Function: fstatSync],
//   fsync: [Function: fsync],
//   fsyncSync: [Function: fsyncSync],
//   ftruncate: [Function: ftruncate],
//   ftruncateSync: [Function: ftruncateSync],
//   futimes: [Function: futimes],
//   futimesSync: [Function: futimesSync],
//   lchown: [Function: lchown],
//   lchownSync: [Function: lchownSync],
//   lchmod: undefined,
//   lchmodSync: undefined,
//   link: [Function: link],
//   linkSync: [Function: linkSync],
//   lstat: [Function: lstat],
//   lstatSync: [Function: lstatSync],
//   lutimes: [Function: lutimes],
//   lutimesSync: [Function: lutimesSync],
//   mkdir: [Function: mkdir],
//   mkdirSync: [Function: mkdirSync],
//   mkdtemp: [Function: mkdtemp],
//   mkdtempSync: [Function: mkdtempSync],
//   open: [Function: open],
//   openSync: [Function: openSync],
//   opendir: [Function: opendir],
//   opendirSync: [Function: opendirSync],
//   readdir: [Function: readdir],
//   readdirSync: [Function: readdirSync],
//   read: [Function: read],
//   readSync: [Function: readSync],
//   readv: [Function: readv],
//   readvSync: [Function: readvSync],
//   readFile: [Function: readFile],
//   readFileSync: [Function: readFileSync],
//   readlink: [Function: readlink],
//   readlinkSync: [Function: readlinkSync],
//   realpath: [Function: realpath] { native: [Function (anonymous)] },
//   realpathSync: [Function: realpathSync] { native: [Function (anonymous)] },
//   rename: [Function: rename],
//   renameSync: [Function: renameSync],
//   rm: [Function: rm],
//   rmSync: [Function: rmSync],
//   rmdir: [Function: rmdir],
//   rmdirSync: [Function: rmdirSync],
//   stat: [Function: stat],
//   statSync: [Function: statSync],
//   symlink: [Function: symlink],
//   symlinkSync: [Function: symlinkSync],
//   truncate: [Function: truncate],
//   truncateSync: [Function: truncateSync],
//   unwatchFile: [Function: unwatchFile],
//   unlink: [Function: unlink],
//   unlinkSync: [Function: unlinkSync],
//   utimes: [Function: utimes],
//   utimesSync: [Function: utimesSync],
//   watch: [Function: watch],
//   watchFile: [Function: watchFile],
//   writeFile: [Function: writeFile],
//   writeFileSync: [Function: writeFileSync],
//   write: [Function: write],
//   writeSync: [Function: writeSync],
//   writev: [Function: writev],
//   writevSync: [Function: writevSync],
//   Dir: [class Dir],
//   Dirent: [class Dirent],
//   Stats: [Function: Stats],
//   ReadStream: [Getter/Setter],
//   WriteStream: [Getter/Setter],
//   FileReadStream: [Getter/Setter],
//   FileWriteStream: [Getter/Setter],
//   _toUnixTimestamp: [Function: toUnixTimestamp],
//   F_OK: 0,
//   R_OK: 4,
//   W_OK: 2,
//   X_OK: 1,
//   constants: [Object: null prototype] {
//     UV_FS_SYMLINK_DIR: 1,
//     UV_FS_SYMLINK_JUNCTION: 2,
//     O_RDONLY: 0,
//     O_WRONLY: 1,
//     O_RDWR: 2,
//     UV_DIRENT_UNKNOWN: 0,
//     UV_DIRENT_FILE: 1,
//     UV_DIRENT_DIR: 2,
//     UV_DIRENT_LINK: 3,
//     UV_DIRENT_FIFO: 4,
//     UV_DIRENT_SOCKET: 5,
//     UV_DIRENT_CHAR: 6,
//     UV_DIRENT_BLOCK: 7,
//     S_IFMT: 61440,
//     S_IFREG: 32768,
//     S_IFDIR: 16384,
//     S_IFCHR: 8192,
//     S_IFLNK: 40960,
//     O_CREAT: 256,
//     O_EXCL: 1024,
//     UV_FS_O_FILEMAP: 536870912,
//     O_TRUNC: 512,
//     O_APPEND: 8,
//     F_OK: 0,
//     R_OK: 4,
//     W_OK: 2,
//     X_OK: 1,
//     UV_FS_COPYFILE_EXCL: 1,
//     COPYFILE_EXCL: 1,
//     UV_FS_COPYFILE_FICLONE: 2,
//     COPYFILE_FICLONE: 2,
//   },
//   promises: [Getter]
// }


// menuliskan string ke file (synchronous)
try {
    fs.writeFileSync('data/test.txt', 'Hello World secara synchronous!');
} catch(e) {
  console.log(e);
}

// outputnya akan spt ini :
// Windows@DESKTOP-JN9OIM9 MINGW64 ~/Desktop/belajar-nodejs/core-modules
// $ node app
// Error: ENOENT: no such file or directory, open 'data/test.txt'
//     at Object.openSync (node:fs:585:3)
//     at Object.writeFileSync (node:fs:2170:35)
//     at Object.<anonymous> (C:\Users\Windows\Desktop\belajar-nodejs\core-modules\app.js:8:8)
//     at Module._compile (node:internal/modules/cjs/loader:1105:14)
//     at Object.Module._extensions..js (node:internal/modules/cjs/loader:1159:10)        
//     at Module.load (node:internal/modules/cjs/loader:981:32)
//     at Function.Module._load (node:internal/modules/cjs/loader:822:12)
//     at node:internal/main/run_main_module:17nMain] (node:internal/modules/run_main:77:1:47 {
//   errno: -4058,                             :47 {
//   syscall: 'open',
//   code: 'ENOENT',
//   path: 'data/test.txt'
// }


// menuliskan string ke file bertype asynchronous
// fs.writeFile('data/test.txt', 'Hello World secara Asynchronous', (e) => {
//   console.log(e);
// })
// outputnya :
// Windows@DESKTOP-JN9OIM9 MINGW64 ~/Desktop/belajar-nodejs/core-modules GW64 ~/Desktop/belajar-nodejs/core-modules
// $ node app
// null     

// cara install packages npm
// ===> npm i(install) name_packages
// ===> npm uninstall name_packages
// ===> npm i name_packages@version