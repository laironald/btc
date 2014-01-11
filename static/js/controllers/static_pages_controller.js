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


app.controller("IndexController", ['$scope', '$rootScope', function($scope, $rootScope) {
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
	$rootScope.$on("CHANGE_PAGE", function(evt, args) {
		$scope.page = args.page;
	});
}]);

app.controller("HomeController", ['$scope', '$rootScope', function($scope, $rootScope) {
	$rootScope.$broadcast("CHANGE_PAGE", { page: "home" });
}]);

app.controller("UserController", ['$scope', '$rootScope', function($scope, $rootScope) {
	$rootScope.$broadcast("CHANGE_PAGE", { page: "user" });
}]);

app.controller("ActionController", ['$scope', '$rootScope', function($scope, $rootScope) {
	$rootScope.$broadcast("CHANGE_PAGE", { page: "action" });
}]);

app.controller("AnalysisController", ['$scope', '$rootScope', function($scope, $rootScope) {
	$rootScope.$broadcast("CHANGE_PAGE", { page: "analysis" });
}]);
