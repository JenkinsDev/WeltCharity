# Validatinator

Current Release: 1.1.1-beta

Validatinator is a simple, yet effective, vanilla JavaScript form validation "plugin." Validatinator is based off of one of PHP's most famous framework, Laravel.  Using Validatinator is as easy as instantiating a Validatinator object, calling the passes or fails methods and if there are failed validations then grabbing those validations from the errors property on the main object.

#### Table of Contents
* [Setting Up](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up)
    * [Bower Method](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-bower-method)
        * [1 Step Wonder](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-1-step-wonder)
    * [Original Method](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-original-method)
        * [Downloading The Source](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-download-the-source)
        * [Running The Source Through Jasmine Tests (Optional)](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-running-the-source-through-jasmine-testing-optional)
        * [Linking The JavaScript](https://github.com/JenkinsDev/Validatinator/wiki/Setting-Up#wiki-linking-the-javascript-files)
* [Using Validatinator](https://github.com/JenkinsDev/Validatinator/wiki/Using-Validatinator)
    * [Instantiating The Validatinator Object](https://github.com/JenkinsDev/Validatinator/wiki/Using-Validatinator#wiki-instantiating-a-validatinator-object)
    * [Validating The Form](https://github.com/JenkinsDev/Validatinator/wiki/Using-Validatinator#wiki-validating-the-form)
    * [Getting Validation Error Messages](https://github.com/JenkinsDev/Validatinator/wiki/Using-Validatinator#wiki-getting-validation-error-messages)
* [Customizing Validatinator](https://github.com/JenkinsDev/Validatinator/wiki/Customizing-Validatinator)
    * [Adding Custom Validation Methods](https://github.com/JenkinsDev/Validatinator/wiki/Customizing-Validatinator#wiki-adding-custom-validation-methods)
    * [Adding Custom Validation Error Messages](https://github.com/JenkinsDev/Validatinator/wiki/Customizing-Validatinator#wiki-adding-custom-validation-error-messages)
* [Validation Methods](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods)
    * [Accepted](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-accepted)
    * [Alpha](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-alpha)
    * [Alpha Dash](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-alpha-dash)
    * [Alpha Numeric](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-alpha-numeric)
    * [Between](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-between)
    * [Between Length](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-between-length)
    * [Contains](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-contains)
    * [Different](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-different)
    * [Digits Length](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-digits-length)
    * [Digits Length Between](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-digits-length-between)
    * [Email](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-email)
    * [IPv4](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-ipv4)
    * [Max](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-max)
    * [Max Length](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-max-length)
    * [Min](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-min)
    * [Min Length](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-min-length)
    * [Not In](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-not-in)
    * [Number](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-number)
    * [Required](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-required)
    * [Required If](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-required-if)
    * [Required If Not](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-required-if-not)
    * [Same](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-same)
    * [URL](https://github.com/JenkinsDev/Validatinator/wiki/Validation-Methods#wiki-url)
