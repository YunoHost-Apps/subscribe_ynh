<html>
<head>    
    <meta name="robots" content="noindex, nofollow">
    <meta charset="utf-8">
    <link rel="shortcut icon" href="icons/favicon.ico">
    <link href="css/artichaut.css" rel="stylesheet">
    <link href="css/artichaut-col.css" rel="stylesheet">
    <link href="css/artichaut-messages.css" rel="stylesheet">
    <link href="css/artichaut-buttons.css" rel="stylesheet">
    <link href="css/fonts.css" rel="stylesheet">
    <link href="css/ynh-style.css" rel="stylesheet">
    <style>
        #mail{
            width:50%;
        }
    </style>
</head>
<body>

    <h1 id="logo" class="logo">
        <img src="img/logo-ynh-white.svg"/><span class="element-invisible">Yunohost</span>
    </h1>

    <div class="overlay">
        <div class="wrapper login">
            <form action="/yunohost/api/subscriptions" method="POST" class="login-form">
                <div class="form-group">
                    <label class="icon icon-user" for="username">
                        <span class="element-invisible">Nom d'utilisateur</span>
                    </label>
                    <input id="user" name="username" type="text" value="" class="form-control form-text" 
                    placeholder="Nom d'utilisateur" required/>
                </div>
                <div class="form-group">
                    <label class="icon icon-user" for="firstname">
                        <span class="element-invisible">Prénom</span>
                    </label>
                    <input id="firstname" name="firstname" type="text" value="" class="form-control form-text"
                    placeholder="Prénom" required/>
                </div>
                <div class="form-group">
                    <label class="icon icon-user" for="lastname">
                        <span class="element-invisible">Nom</span>
                    </label>
                    <input id="lastname" name="lastname" type="text" value="" class="form-control form-text"
                    placeholder="Nom" required/>
                </div>
                <div class="form-group">
                    <label class="icon icon-mail" for="mail">
                        <span class="element-invisible">Mail</span>
                    </label>
                    <input id="mail" name="mail" type="text" value="" class="form-control form-text"
                    placeholder="Mail" required/> @yunohost.local
                </div>
                <div class="form-group">
                    <label class="icon icon-lock" for="password">
                        <span class="element-invisible">Mot de passe</span>
                    </label>
                    <input id="password" name="password" type="password" value="" class="form-control form-text"
                    placeholder="Mot de passe" required/>
                </div>
                <div class="form-group">
                    <label class="icon icon-lock" for="passwordagain">
                        <span class="element-invisible">Confirmation du mot de passe</span>
                    </label>
                    <input id="passwordagain" name="passwordagain" type="password" value="" class="form-control form-text"
                    placeholder="Confirmation du mot de passe" required/>
                </div>
                <input name="submit" type="submit" value="S'inscrire" class="btn classic-btn large-btn" />
            </form>
        </div>
    </div>
    <script src="js/global.js"></script>
</body></html>
