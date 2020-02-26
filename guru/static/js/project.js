/* Project specific Javascript goes here. */

(function() {
    "use strict";

    const langDropdownNode = $("#lang-dropdown");
    const curLangNode = langDropdownNode.find("button");
    const langOptionsMap = langDropdownItems();
    const topSubdomain = window.location.host[0].toLowerCase();
    const curLanguage = (topSubdomain in langOptionsMap ? topSubdomain : "En");

    (function () {
        /* -----------------------------------------------
            Adjust language dropdown based on subdomain
        ----------------------------------------------- */
        const origLang = curLangNode.text;
        curLangNode.text = curLanguage;
        langOptionsMap[curLanguage] = origLang;
    })();

    function langDropdownItems() {
        const langOptions = langDropdownNode.find("div").children();
        let langNodeMap = {};
        // iterate over language dropdown options
        for (let i=0; i<langOptions.length; i++) {
            const node = langOptions[i];
            const optionText = node.text.toLowerCase();
            langNodeMap[optionText] = node;
        }
        return langNodeMap;
    }
})();
