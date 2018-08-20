(function($) {
    
    $.dotdotdot = function(el, options) {
        var base = this;
        base.$el = $(el);
        base.$el.data("dotdotdot", base);
        base.dotItUp = function($element, maxDots) {
            if ($element.text().length == maxDots) {
                $element.text("");
            } else {
                $element.append(".");
            }
        };
        
        base.stopInterval = function() {    
            clearInterval(base.theInterval);
			base.theInterval = undefined;
        };
        
        base.init = function() {
        
            if ( typeof( speed ) === "undefined" || speed === null ) speed = 300;
            if ( typeof( maxDots ) === "undefined" || maxDots === null ) maxDots = 3;
            
            base.speed = speed;
            base.maxDots = maxDots;
                                    
            base.options = $.extend({},$.dotdotdot.defaultOptions, options);
                        
            base.$el.html("");
            
            //base.$dots = base.$el.find("span");
			base.$dots = base.$el;
            
            //base.theInterval = setInterval(base.dotItUp, base.options.speed, base.$dots, base.options.maxDots);
			if(base.theInterval) {
				base.stopInterval();
			}
            base.theInterval = setInterval(function() {
				base.dotItUp(base.$dots, base.options.maxDots);
			}, base.options.speed);
        };
        
        base.init();
    
    };
    
    $.dotdotdot.defaultOptions = {
        speed: 300,
        maxDots: 3
    };
    
    $.fn.dotdotdot = function(options) {
        
        if (typeof(options) == "string") {
			this.each(function() {
				var safeGuard = $(this).data('dotdotdot');
				if (safeGuard) {
					safeGuard.stopInterval();
				}
			});
        } else { 
            return this.each(function(){
                (new $.dotdotdot(this, options));
            });
        } 
        
    };
    
})(jQuery);