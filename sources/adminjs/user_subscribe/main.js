var UserSubscribe = function(app,path) { 
    app.get('#/subscriptions', function (c) {		      
		c.api('/subscriptions', function(data) {
            c.api('/users', function(data2) { 
                data['users']=data2['users']
                c.view([path,'subscription/subscription_list'], data);
            }); 
        });
    });  
};
