// Bootstrap Alert Helper

bootstrap_alert = function() {}
bootstrap_alert.message = function(message, category='primary') {
    $('#alerts').append('<div class="alert alert-' + category + ' alert-dismissible fade show" role="alert">' + 
    message +
    '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>' +
    '</div>');
}

bootstrap_alert.primary = function(message) {
    bootstrap_alert.message(message, 'primary');
}

bootstrap_alert.secondary = function(message) {
    bootstrap_alert.message(message, 'secondary');
}

bootstrap_alert.success = function(message) {
    bootstrap_alert.message(message, 'success');
}

bootstrap_alert.danger = function(message) {
    bootstrap_alert.message(message, 'danger');
}

bootstrap_alert.warning = function(message) {
    bootstrap_alert.message(message, 'warning');
}

bootstrap_alert.info = function(message) {
    bootstrap_alert.message(message, 'info');
}

bootstrap_alert.light = function(message) {
    bootstrap_alert.message(message, 'light');
}

bootstrap_alert.dark = function(message) {
    bootstrap_alert.message(message, 'dark');
}
