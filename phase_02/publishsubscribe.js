
/* JS functions for handling start and change of events*/

var incidents = {
  incidents: {},
  start: function (Nameofincident, instance) {
    this.incidents[Nameofincident] = this.incidents[Nameofincident] || [];
    this.incidents[Nameofincident].push(instance);
  },
  change: function (Nameofincident, info) {
    if (this.incidents[Nameofincident]) {
      this.incidents[Nameofincident].forEach(function(instance) {
        instance(info);
      });
    }
  }
};
