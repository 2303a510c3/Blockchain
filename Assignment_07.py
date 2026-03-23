<!DOCTYPE html>
<html>
<head>
<title>Personal Portfolio dApp</title>

<script src="https://cdn.jsdelivr.net/npm/web3@1.7.5/dist/web3.min.js"></script>

<style>

body{
    font-family: Arial;
    background:#f2f2f2;
    text-align:center;
}

.container{
    margin:auto;
    margin-top:80px;
    width:350px;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px gray;
}

button{
    padding:10px 20px;
    background:#4CAF50;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}

.info{
    margin-top:20px;
    font-size:18px;
}

</style>

</head>

<body>

<div class="container">

<h2>Blockchain Portfolio</h2>

<button onclick="connectWallet()">Connect MetaMask</button>

<div class="info">
<p><b>Name:</b> <span id="name">-</span></p>
<p><b>Role:</b> <span id="role">-</span></p>
<p><b>Skills:</b> <span id="skills">-</span></p>
</div>

</div>

<script>

async function connectWallet(){

if(window.ethereum){

const web3 = new Web3(window.ethereum);

await window.ethereum.request({method:'eth_requestAccounts'});

const accounts = await web3.eth.getAccounts();

document.getElementById("name").innerText = "Aman Sarkar";
document.getElementById("role").innerText = "Blockchain Developer";
document.getElementById("skills").innerText = "Solidity, Web3.js, Ethereum, HTML, CSS, JavaScript";

alert("Wallet Connected: " + accounts[0]);

}
else{
alert("Please install MetaMask");
}

}
</script>
</body>
</html>