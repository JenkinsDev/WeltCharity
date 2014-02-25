(function($, window, undefined) {
    $(document).ready(function() {
    	/**
    	 * Quick jQuery method of enabling mouse-over showing of the
    	 * multi-tiered navbar for bootstrap.
    	 */
        $('.nav').on('mouseenter', '.dropdown', function() {
            $(this).addClass('open');
        }).on('mouseleave', '.dropdown', function() {
        	$(this).removeClass('open');
        });
    });
})(jQuery, window, undefined)