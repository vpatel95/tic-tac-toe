'use strict';

/**
 * @ngdoc object
 * @name ticTacToeApp
 * @requires $routeProvider
 * @requires ticTacToeControllers
 *
 * @description
 * Root app, which routes and specifies the partial html and controller depending on the url requested.
 *
 */
var app = angular.module('ticTacToeApp',
    ['ticTacToeControllers', 'ngRoute']).
    config(['$routeProvider',
        function ($routeProvider) {
            $routeProvider.
                when('/', {
                    templateUrl: '/partials/home.html'
                }).
                otherwise({
                    redirectTo: '/'
                });
        }]);