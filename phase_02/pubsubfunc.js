(function(){
	//Caching the DOM elements
	var $element = $('#add_rem_pub')
	var template = $element.html() // get the index.html template that we have designed

	//binding the incidents
	$element.delegate('button','click',incident_operation) //S and O in the same module. So delegate function instead of start

	render()

	function incident_operation(incident){

		name_pub = $element.find('input')[0].value
		$currentElement = $(incident.target)
		operation_addorrem = $currentElement.html().toLowerCase()
		incidents.change(operation_addorrem+"_publisher" ,name_pub)
		render()
	}
	// render function is used to make sure all the changes are put in real time
	function render(){
		$element.find('input').val('')
	}
})();

;(function($){
	//Caching the DOM elements
	var $element = $('#add_rem_sub')
	var template = $element.html()

	//binding the incidents
	$element.delegate('button','click',incident_operation) //S and O in the same module. So delegate function used instead of start.

	render()

	function incident_operation(incident){

		name_sub = $element.find('input')[0].value // name of the subscriber
		$currentElement = $(incident.target)
		operation_addorrem = $currentElement.html().toLowerCase() //is it add or remove? which operation? operation =  add | remove
		//incident_change =  add_subscriber | remove_subscriber
		incidents.change(operation_addorrem+ '_subscriber',name_sub)
		render()
	}

	function render(){
		$element.find('input').val('')
	}
})(jQuery); // jQuery passed for protection from other libraries that use dollar symbols.



var Publisher = (function(){

	var publishers_array = []

	//caching DOM
	var $element = $('#list-of-publishers')
	var template = $element.html()

	//binding incidents (DOM)
	$element.delegate('button','click',Publish_Topic)

	//binding incidents (Publisher and Subscriber)
	incidents.start('add_publisher', add)
	incidents.start('remove_publisher', remove)

	_render();

	//this function makes sure all changes are added in the webpage.
	function _render(){
		info = {
				publishers_array: publishers_array
		}
		$element.html(Mustache.render(template, info))
	}


	//obtains the specific publisher in the array.
	function obtain(pos){
		pos = pos || -1
		if(pos != -1)
			return publishers_array[pos]
		return publishers_array;
	}

	//adds publisher by name.
	function add(name){

		pubs = publishers_array.map(function(pub, pos){
			return pub.name.toLowerCase()
		});

		pos = pubs.indexOf(name.toLowerCase())
		if(pos != -1) {
			alert(name + ' is already a publisher!')
			return
		}

		publishers_array.push({'name' : name})
		_render()
	}
	//removes a publisher.
	function remove(pub){
		pubs = publishers_array.map(function(publisher){
			return publisher.name;
		});

		pos = pubs.indexOf(pub);

		if(pos != -1) {
			publishers_array.splice(pos, 1)
			_render()
		}
	}

	//sends
	function Advertise_Topic(incident){
        $currentElement = $(incident.target)
        $pub = $currentElement.closest('.publisher');
        name = $pub.find('h5').html();
        TopicName = $pub.find('input')[0].value;
        Details = $pub.find('textarea')[0].value;

		section = {
			'name':name,
			'TopicName': TopicName,
			'Details': Details
		};

		pubs = publishers_array.map(function(publisher){
			return publisher.name;
		});

		pos = pubs.indexOf(section.name);

		publishers_array[pos].Tweets = publishers_array[pos].Tweets || []

		publishers_array[pos].Tweets.push({
			'TopicName':TopicName,
			'Details':Details
		});

		_render();

		incidents.change('notify', section)
	}


//publishes a topic of interest.
	function Publish_Topic(incident){
        $currentElement = $(incident.target)
        $pub = $currentElement.closest('.publisher');
        name = $pub.find('h5').html();
        TopicName = $pub.find('input')[0].value;
        Details = $pub.find('textarea')[0].value;

		section = {
			'name':name,
			'TopicName': TopicName,
			'Details': Details
		};

		pubs = publishers_array.map(function(publisher){
			return publisher.name;
		});

		pos = pubs.indexOf(section.name);

		publishers_array[pos].Tweets = publishers_array[pos].Tweets || []

		publishers_array[pos].Tweets.push({
			'TopicName':TopicName,
			'Details':Details
		});

		_render();

		incidents.change('notify', section)
	}

	return {
		obtain: obtain,
		Publish_Topic: Publish_Topic
	}

})();




var Subscriber = (function(){

	var subscribers_array = [];

	var $element = $('#list-of-subscribers')
	var template = $element.html()

	//binding the incidents

	//delegate function used as S and O are in the same module.
	$element.delegate('button','click',Subscribe_Topic)

	// start function used from publishsubscribe.js as now we are dealing with stuffs in different module.
	incidents.start('notify', notify_listener)
	incidents.start('add_subscriber', add)
	incidents.start('remove_subscriber', remove)


	//make sure all changes are accounted.
	_render()

	function _render(){
		info = {
				subscribers_array: subscribers_array
		}

		$element.html(Mustache.render(template, info))
	}

	function obtain(pos){
		pos = pos || -1
		if(pos != -1)
			return subscribers_array[pos]
		return subscribers_array;
	}


	//this function adds a subscriber
	function add(name){
		subs = subscribers_array.map(function(sub, pos){
			return sub.name.toLowerCase()
		});


		pos = subs.indexOf(name.toLowerCase())
		if(pos != -1) {
			alert(name + ' is already there in the database. Please enter a new username.')
			return
		}

		subscribers_array.push({'name' : name})
		_render()
	}

	//this function removes a subscriber from the list/
	function remove(name){
		subs = subscribers_array.map(function(sub, pos){
			return sub.name
		});

		pos = subs.indexOf(name)

		if(pos != -1) {
			subscribers_array.splice(pos, 1)
			_render()
			return
		}

		alert(name + ' does not exist currently. Maybe you typed a mistyped the case?')
	}

	function notify_listener(info){
		subscribers_array.forEach(function(sub, pos){
			sub.TopicNames = sub.TopicNames || []
			sub.sub_notif_list = sub.sub_notif_list || []
			if(sub.TopicNames.indexOf(info.TopicName) != -1)
				sub.sub_notif_list.push(info)
		});

		_render()
	}

	// this function adds a new TopicName, that is subsribes.
	function Subscribe_Topic(incident){
        $currentElement = $(incident.target)
        $sub = $currentElement.closest('.subscriber');
        name = $sub.find('h5').html();
        TopicName = $sub.find('input')[0].value;

		subscribers_array.forEach(function(sub, pos){
			if(name.toLowerCase() == sub.name.toLowerCase()){
				sub.TopicNames = sub.TopicNames || [] //There are no TopicNames array for a new subscribers array. So initialize an empty list []
				if(sub.TopicNames.indexOf(TopicName) == -1){
					sub.TopicNames.push(TopicName);
					_render()
					return;
				}
			}
		});
	}

	return{
		obtain: obtain,

	}
})();
