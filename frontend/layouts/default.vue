<template>
  <div>
    <header-nav />

    <nuxt />
    <footer-nav />
  </div>
</template>

<script>
import HeaderNav from '~/components/HeaderNav'
import FooterNav from '~/components/FooterNav'

export default {
  components: {
    HeaderNav,
    FooterNav,
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=M+PLUS+Rounded+1c:400,500');
html {
  font-family: 'M PLUS Rounded 1c', sans-serif;
  color: #343434;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
  background-color: #ffffff;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
</style>
