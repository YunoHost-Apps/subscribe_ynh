app = Sammy('#main', function (sam) {

    /**
     * Sammy Configuration
     *
     */
    // Plugins
    sam.use('Handlebars', 'ms');

    
    Handlebars.registerHelper('t', function(y18n_key) {
      var result = y18n.t(y18n_key, Array.prototype.slice.call(arguments, 1));
      return new Handlebars.SafeString(result);
    });

    /**
     * Helpers
     *
     */
    sam.helpers({

       
        // API call
        api: function(uri, callback, method, data, websocket) {
            c = this;

            call = function(uri, callback, method, data) {
                method = typeof method !== 'undefined' ? method : 'GET';
                data   = typeof data   !== 'undefined' ? data   : {};
                if (window.navigator && window.navigator.language && (typeof data.locale === 'undefined')) {
                    data.locale = window.navigator.language;
                }

                var args = data;
                jQuery.ajax({
                    url: uri,
                    type: method,
                    crossdomain: true,
                    data: data,
                    traditional: true,
                    dataType: 'json',
                    // beforeSend: function(req) {
                    //     req.setRequestHeader('Authorization', auth);
                    // }
                })
                .always(function(xhr, ts, error) {
                })
                .done(function(data) {
                    data = data || {};
                    callback(data);
                })
                .fail(function(xhr) {
                    if (xhr.status == 200) {
                        callback({});
                    } else if (typeof xhr.responseJSON !== 'undefined') {
                        //c.flash('fail', xhr.responseJSON.error);
                    } else if (typeof xhr.responseText !== 'undefined' && uri !== '/postinstall') {
                        //c.flash('fail', xhr.responseText);
                    } else {
                         //c.flash('fail', y18n.t('error_server'));
                    }
                });
            }

            call(uri, callback, method, data);
        },

        // Render view (cross-browser)
        view: function (view, data, callback) {
            callback = typeof callback !== 'undefined' ? callback : function() {};
            baseView='';
            
            rendered = this.render(baseView+'views/'+view+'.ms', data);
            console.log("views");
            rendered.appendTo($( "#content" ))
            rendered.swap(function(){
                callback()
                // Force scrollTop on page load
                $('html, body').scrollTop(0);
            });
        }
    });


    
    /**
     * Errors
     */
    sam.notFound = function(){
        // Redirect to home page on 404.
        window.location = '#/';
    };


    sam.get('#/', function (c) {
        c.view('subscribe',{'domain': window.location.hostname});
    });

    sam.post('#/', function (c) {
        params = {
            'username': c.params['username'],
            'firstname': c.params['firstname'],
            'lastname': c.params['lastname'],
            'mail': c.params['mail'],
            'password': c.params['password'],
            'passwordagain': c.params['passwordagain'],
            'info': c.params['info']
        }
        c.api('/yunohost/api/subscriptions', function(data) {
            c.view('subscribed');
        }, 'POST', params, false);
    });

});



/**
 * Run the app
 *
 */

$(document).ready(function () {

    var concatObject= function (o1,o2) {
		for(var k in o2) o1[k]=o2[k];
	}
	// Default language
	y18n.translations['en']={};
	$.getJSON('locales/en.json', function(data){
		concatObject(y18n.translations['en'], data);
	});
	
	// User language
	if (y18n.locale !== 'en') {
		y18n.translations[y18n.locale]={};
		$.getJSON('locales/'+ y18n.locale +'.json', function(data){
			concatObject(y18n.translations[y18n.locale], data);
		});
	}
    
	app.run('#/');
});
