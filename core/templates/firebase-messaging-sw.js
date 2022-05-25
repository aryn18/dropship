importScripts("https://www.gstatic.com/firebasejs/9.8.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/9.8.1/firebase-messaging.js");


firebase.initializeApp({
    apiKey: "AIzaSyB7Cm3LgiY5KOpy8tgRB8SE9vE6Kc8fETo",
    authDomain: "dropship-f1ad9.firebaseapp.com",
    projectId: "dropship-f1ad9",
    storageBucket: "dropship-f1ad9.appspot.com",
    messagingSenderId: "161989651929",
    appId: "1:161989651929:web:fad9968a82ac7c7cd7fdc8"
});

const messaging = firebase.messaging();