<script setup lang="ts">
import {onMounted, reactive, ref} from "vue";
import translate from "../composables/translator";
import tokenize, {Token} from "../composables/tokenizer";

const translation = ref('translation here')
const tokens = ref([] as Token[])

onMounted(() => {
  // translate('寿司を食べたい')
  //     .then(data => {
  //       translation.value = data
  //     })
  //     .catch(err => console.error(err))

  tokenize('今日は寿司を食べたい')
      .then(data => {
        for (const elem of data) {
          tokens.value.push(elem)
        }
      })
      .catch(err => console.error(err))
})
</script>

<template>
  <div>
    <div>Reader Page</div>
    <div>{{ translation }}</div>
    <div>{{ tokens }}</div>
  </div>

</template>

<style scoped>

</style>