function loginJS() {
    var login = document.getElementById("login").value;
    var password = document.getElementById("password").value;
    eel.login(login, password);
}

eel.expose(loginSuccess);
function loginSuccess() {
    var text1 = document.getElementById('login');
    var text2 = document.getElementById('password');
    var button1 = document.getElementById('submit');
    text1.style.display = 'none';
    text2.style.display = 'none';
    button1.style.display = 'none';
    document.getElementById("statusText").innerHTML = "Logged in Successfuly!";
}

eel.expose(loginTry);
function loginTry() {
    document.getElementById("statusText").innerHTML = "User doesn't exist or wrong password! Try again.!";
}

eel.expose(privMenu)
function privMenu() {
    document.getElementById("statusText").innerHTML = "Menu";
    document.getElementById("subText").innerHTML = "Select a function.";
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('settings');
    var button4 = document.getElementById('logout');
    button1.style.display = 'inline-block';
    button2.style.display = 'inline-block';
    button3.style.display = 'inline-block';
    button4.style.display = 'inline-block';
    var fileNText = document.getElementById('fileNameStr');
    var uploadButtonSubmit = document.getElementById('uploadSubmit');
    var backButtonSubmit = document.getElementById('backButton');
    fileNText.style.display = 'none';
    uploadButtonSubmit.style.display = 'none';
    backButtonSubmit.style.display = 'none';
    var searchText = document.getElementById('searchQuery');
    var searchButton = document.getElementById('searchButton');
    var downloadButton = document.getElementById('downloadButton');
    searchText.style.display = 'none';
    searchButton.style.display = 'none';
    downloadButton.style.display = 'none';
    var addUser = document.getElementById('addUserButton');
    var delUser = document.getElementById('deleteUserButton');
    var newKey = document.getElementById('newKey');
    addUser.style.display = 'none';
    delUser.style.display = 'none';
    newKey.style.display = 'none';
    var addUserName = document.getElementById('addUserName');
    var addPassword = document.getElementById('addPassword');
    var createUser = document.getElementById('createUser');
    addUserName.style.display = 'none';
    addPassword.style.display = 'none';
    createUser.style.display = 'none';
    var deleteUser = document.getElementById('deleteUser');
    deleteUser.style.display = 'none';

}

eel.expose(standardMenu)
function standardMenu() {
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('logout');
    button1.style.display = 'inline-block';
    button2.style.display = 'inline-block';
    button3.style.display = 'inline-block';
    var text1 = document.getElementById('fileNameStr');
    var button5 = document.getElementById('uploadSubmit');
    var button6 = document.getElementById('backButton');
    text1.style.display = 'none';
    button5.style.display = 'none';
    button6.style.display = 'none';
    var searchText = document.getElementById('searchQuery');
    var searchButton = document.getElementById('searchButton');
    var downloadButton = document.getElementById('downloadButton');
    searchText.style.display = 'none';
    searchButton.style.display = 'none';
    downloadButton.style.display = 'none';

}


function uploadScreen() {
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('settings');
    var button4 = document.getElementById('logout');
    button1.style.display = 'none';
    button2.style.display = 'none';
    button3.style.display = 'none';
    button4.style.display = 'none';
    var text1 = document.getElementById('fileNameStr');
    var button5 = document.getElementById('uploadSubmit');
    var button6 = document.getElementById('backButton');
    text1.style.display = 'inline-block';
    button5.style.display = 'inline-block';
    button6.style.display = 'inline-block';
    document.getElementById("statusText").innerHTML = "Encrypt and Upload Files";
    document.getElementById("subText").innerHTML = "Ensure that files you wish to upload are in the 'Files' folder.";
}

function downloadScreen() {
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('settings');
    var button4 = document.getElementById('logout');
    button1.style.display = 'none';
    button2.style.display = 'none';
    button3.style.display = 'none';
    button4.style.display = 'none';
    var searchText = document.getElementById('searchQuery');
    var searchButton = document.getElementById('searchButton');
    var downloadButton = document.getElementById('downloadButton');
    var button6 = document.getElementById('backButton');
    searchText.style.display = 'inline-block';
    searchButton.style.display = 'inline-block';
    downloadButton.style.display = 'inline-block';
    button6.style.display = 'inline-block';
    document.getElementById("statusText").innerHTML = "Download and Decrypt Files";
    document.getElementById("subText").innerHTML = "Files are downloaded to Downloads folder.";
}

function settingScreen() {
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('settings');
    var button4 = document.getElementById('logout');
    button1.style.display = 'none';
    button2.style.display = 'none';
    button3.style.display = 'none';
    button4.style.display = 'none';
    var addUser = document.getElementById('addUserButton');
    var delUser = document.getElementById('deleteUserButton');
    var newKey = document.getElementById('newKey');
    var button6 = document.getElementById('backButton');
    addUser.style.display = 'inline-block';
    delUser.style.display = 'inline-block';
    newKey.style.display = 'inline-block';
    button6.style.display = 'inline-block';
    document.getElementById("statusText").innerHTML = "Download and Decrypt Files";
    document.getElementById("subText").innerHTML = "Files are downloaded to Downloads folder.";
}


function addUserScreen() {
    var addUser = document.getElementById('addUserButton');
    var delUser = document.getElementById('deleteUserButton');
    var newKey = document.getElementById('newKey');
    var button6 = document.getElementById('backButton');
    addUser.style.display = 'none';
    delUser.style.display = 'none';
    newKey.style.display = 'none';

    var addUserName = document.getElementById('addUserName');
    var addPassword = document.getElementById('addPassword');
    var createUser = document.getElementById('createUser');


    addUserName.style.display = 'inline-block';
    addPassword.style.display = 'inline-block';
    createUser.style.display = 'inline-block';
    button6.style.display = 'inline-block';
}

function deleteUserScreen() {
    var addUser = document.getElementById('addUserButton');
    var delUser = document.getElementById('deleteUserButton');
    var newKey = document.getElementById('newKey');
    var button6 = document.getElementById('backButton');
    addUser.style.display = 'none';
    delUser.style.display = 'none';
    newKey.style.display = 'none';

    var addUserName = document.getElementById('addUserName');
    var deleteUser = document.getElementById('deleteUser');


    addUserName.style.display = 'inline-block';
    deleteUser.style.display = 'inline-block';
    button6.style.display = 'inline-block';
}



function backButtonClick() {
    eel.loopBreak();
}


function logOut() {
    eel.logOutPy();
    eel.loopBreak();
    var loginText = document.getElementById('login');
    var passText = document.getElementById('password');
    var loginButton = document.getElementById('submit');
    loginText.style.display = 'inline-block';
    passText.style.display = 'inline-block';
    loginButton.style.display = 'inline-block';
    var button1 = document.getElementById('upload');
    var button2 = document.getElementById('download');
    var button3 = document.getElementById('settings');
    var button4 = document.getElementById('logout');
    button1.style.display = 'none';
    button2.style.display = 'none';
    button3.style.display = 'none';
    button4.style.display = 'none';
    var fileNText = document.getElementById('fileNameStr');
    var uploadButtonSubmit = document.getElementById('uploadSubmit');
    var backButtonSubmit = document.getElementById('backButton');
    fileNText.style.display = 'none';
    uploadButtonSubmit.style.display = 'none';
    backButtonSubmit.style.display = 'none';


    document.getElementById("statusText").innerHTML = "Secure The Cloud";
    document.getElementById("subText").innerHTML = "Don't be a fool encrypt your data.";
}

function uploadClick() {
    var file = document.getElementById('fileNameStr').value;
    eel.encrypt(file);
    eel.uploadFile(file);

}

function searchClick() {
    var file = document.getElementById('searchQuery').value;
    eel.searchFile(file)
}

function downloadClick() {
    var file = document.getElementById('searchQuery').value;
    eel.printToConsole(file);
    eel.downloadFile(file);
    eel.decrypt(file);
}

function createUserButton() {
    var userName = document.getElementById('addUserName').value;
    var password = document.getElementById('addPassword').value;
    eel.newUser(userName, password);
}

function deleteUserClick() {
    var userName = document.getElementById('addUserName').value;
    eel.deleteUser(userName);
}

function newKeyGen() {
    eel.keyGen();
}