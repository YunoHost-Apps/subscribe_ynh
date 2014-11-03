<form id="form" action="#/" method="POST" class="login-form">
    <div class="form-group">
        <label class="icon icon-user" for="username">
            <span class="element-invisible">{{t 'username'}}</span>
        </label>
        <input id="user" name="username" type="text" value="" class="form-control form-text" 
        placeholder="{{t 'username'}}" required/>
    </div>
    <div class="form-group">
        <label class="icon icon-user" for="firstname">
            <span class="element-invisible">{{t 'firstname'}}</span>
        </label>
        <input id="firstname" name="firstname" type="text" value="" class="form-control form-text"
        placeholder="{{t 'firstname'}}" required/>
    </div>
    <div class="form-group">
        <label class="icon icon-user" for="lastname">
            <span class="element-invisible">{{t 'lastname'}}</span>
        </label>
        <input id="lastname" name="lastname" type="text" value="" class="form-control form-text"
        placeholder="{{t 'lastname'}}" required/>
    </div>
    <div class="form-group">
        <label class="icon icon-mail" for="mail">
            <span class="element-invisible">{{t 'mail'}}</span>
        </label>
        <input id="mail" name="mail" type="text" value="" class="form-control form-text"
        placeholder="{{t 'mail'}}" required style="display:inline"/> @{{domain}}
    </div>
    <div class="form-group">
        <label class="icon icon-lock" for="password">
            <span class="element-invisible">{{t 'password'}}</span>
        </label>
        <input id="password" name="password" type="password" value="" class="form-control form-text"
        placeholder="{{t 'password'}}" required/>
    </div>
    <div class="form-group">
        <label class="icon icon-lock" for="passwordagain">
            <span class="element-invisible">{{t 'passwordagain'}}</span>
        </label>
        <input id="passwordagain" name="passwordagain" type="password" value="" class="form-control form-text"
        placeholder="{{t 'passwordagain'}}" required/>
    </div>
    <input name="submit" type="submit" value="{{t 'subscribe'}}" class="btn classic-btn large-btn" />
</form>
