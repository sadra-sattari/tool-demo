<?php

if(isset($_POST['sumbit-form'])) 
    {
        $sender_name = $_POST['s-username'];
        $sender_email = $_POST['s-email'];
        $sender_msg_sub = $_POST['s-subject'];
        $sender_msg =  $_POST['txt-box'] ;
        echo $sender_name ;
        
    }
else   
    {
        echo 'not work' ;
    }



?>