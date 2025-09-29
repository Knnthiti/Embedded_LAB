<?php echo "66011390<BR>"; ?>
<?php echo date('d-m-Y H:i:s');?>

<html>

<body>
    <form method="post">
        <p> <button name="sw1on"> GPIO 2 On </button> <button name="sw1off"> GPIO 2 Off</button> </p>
        <p> <button name="sw2on"> GPIO 3 On </button> <button name="sw2off"> GPIO 3 Off</button> </p>
        <p> <button name="sw3on"> GPIO 4 On </button> <button name="sw3off"> GPIO 4 Off</button> </p>
    </form>
</body>

</html>

<?php 
if (isset($_POST['sw1on'])) 
{ 
    system("gpio -g mode 2 out");
    system("gpio -g write 2 1");
} 
else if (isset($_POST['sw1off'])) 
{ 
    system("gpio -g write 2 0");
}
if (isset($_POST['sw2on'])) 
{ 
    system("gpio -g mode 3 out");
    system("gpio -g write 3 1");
} 
else if (isset($_POST['sw2off'])) 
{ 
    system("gpio -g write 3 0");
}
if (isset($_POST['sw3on'])) 
{ 
    system("gpio -g mode 4 out");
    system("gpio -g write 4 1");
} 
else if (isset($_POST['sw3off'])) 
{ 
    system("gpio -g write 4 0");
}
?>