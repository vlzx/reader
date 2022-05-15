<script setup lang="ts">
import {ref, watch} from "vue";
import translate from "../composables/translator";
import tokenize, {Token} from "../composables/tokenizer";
import _ from 'lodash'

const text = ref('')
const translation = ref('')
const tokens = ref([] as Token[])

const update = _.debounce(() => {
    console.log(text.value)
    if (text.value == '') {
      translation.value = ''
      tokens.value = []
      return
    }
    translate(text.value)
        .then(data => {
          translation.value = data
        })
        .catch(err => console.error(err));

    tokenize(text.value)
        .then(data => {
          tokens.value = []
          for (const elem of data) {
            tokens.value.push(elem)
          }
        })
        .catch(err => console.error(err))
  }, 500)

watch(text, () => {
  update()
})
</script>

<template>
  <div>
    <div>Reader Page</div>
    <el-row>
      <el-col :span="12" :offset="6">
        <el-input
            type="textarea"
            v-model="text"
            :autosize="{minRows: 8}"
            resize="none"
            :placeholder="'Type to translate.\nDrag and drop to translate plain text (.txt) file.'"
        ></el-input>
        <div>{{ text ? text : 'text here' }}</div>
        <div>{{ translation ? translation : 'translation here' }}</div>
        <div>tokens: {{ tokens }}</div>
      </el-col>
    </el-row>
  </div>

</template>

<style scoped>

</style>