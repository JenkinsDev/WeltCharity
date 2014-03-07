module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    // Compass adds the ability to automatically transform SCSS to css.
    compass: {
      dev: {
        options: {
          sassDir: '../../scss/',
          cssDir: '../../../css/',
          watch: true
        }
      }
    },
    // Uglify will minify all js files you supply into one file.
    uglify: {
      minify_js: {
        options: {
          banner: "",
          footer: ""
        },
        files: {
          'js/main.min.js': ['dev/js/**.js']
        }
      }
    },
    // CSSMin will minify all css files you supply into one file.
    cssmin: {
      minify_css: {
        options: {
          banner: ""
        },
        files: {
          '../../../css/main.min.css': ['../../../css/main.css']
        }
      }
    },
    // Watch allows us to automate most of our other tasks that don't have polling available.
    watch: {
      jsMin: {
        files: '../../../scripts/main.js',
        tasks: ['uglify:minify_js'],
      },
      cssMin: {
        files: '../../../css/main.css',
        tasks: ['cssmin:minify_css']
      }
    }
  });

  // Load all of our grunt plugins
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task(s).
  grunt.registerTask('default', ['compass']);

};
