var app = angular.module('btc', [
	'ngRoute'
]);

app.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    controller:'HomeController',
    templateUrl:'index_home.html'
  }).when('/user', {
    controller:'UserController',
    templateUrl:'index_user.html'
  }).when('/action', {
    controller:'ActionController',
    templateUrl:'index_action.html'
  }).when('/analysis', {
    controller:'AnalysisController',
    templateUrl:'index_analysis.html'
  }).otherwise({
	  redirectTo:'/'
  });
}]);


app.controller("IndexController", ['$scope', function($scope) {
	$scope.page = "home";
	$scope.links = [{
		href: "https://github.com/laironald/btc",
		name: "GitHub"
	}, {
		href: "https://btc.goideas.org:8888",
		name: "IPython Notebook"
	}, {
		href: "http://bitcoinwisdom.com",
		name: "Bitcoinwisdom"
	}, {
		href: "http://bitcoinity.com/markets",
		name: "Bitcoinity"
	}, {
		href: "http://coindesk.com",
		name: "Coindesk"
	}];
}]);

app.controller("HomeController", ['$scope', function($scope) {
}]);

app.controller("UserController", ['$scope', function($scope) {
}]);

app.controller("ActionController", ['$scope', function($scope) {
}]);

app.controller("AnalysisController", ['$scope', function($scope) {
}]);
