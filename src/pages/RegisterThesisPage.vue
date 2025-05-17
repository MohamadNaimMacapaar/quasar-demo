<template>
  <div class="q-pa-md" style="background: #f7f9fb; min-height: 100vh">
    <!-- Group Members Section -->
    <div class="text-h6 text-bold q-mb-md" style="color: #2d3a4a">Group Member</div>
    <div class="row items-center q-col-gutter-md q-mb-lg">
      <div class="col-3" v-for="(member, idx) in groupMembers" :key="idx">
        <q-card flat bordered class="member-card">
          <q-card-section>
            <div class="row items-center">
              <div class="col">
                <div class="text-caption text-grey-7">Name</div>
              </div>
              <div class="col-auto">
                <q-btn
                  dense
                  flat
                  round
                  icon="delete"
                  color="negative"
                  @click="removeMember(idx)"
                  v-if="groupMembers.length > 1"
                />
              </div>
            </div>
            <q-input
              v-model="member.name"
              dense
              outlined
              placeholder="Enter name"
              class="q-mb-sm"
            />
            <div class="row q-mt-xs">
              <div class="col">
                <div class="text-caption text-grey-7">Year Level</div>
                <q-input
                  v-model="member.year"
                  dense
                  outlined
                  placeholder="Enter year"
                  class="q-mb-sm"
                />
              </div>
              <div class="col">
                <div class="text-caption text-grey-7">ID no.</div>
                <q-input
                  v-model="member.id"
                  dense
                  outlined
                  placeholder="Enter ID"
                  class="q-mb-sm"
                />
              </div>
            </div>
            <div class="q-mt-md text-caption text-grey-7">
              Department:
              <q-input
                v-model="member.department"
                dense
                outlined
                placeholder="Enter department"
                class="q-mt-xs"
              />
            </div>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-auto flex flex-center">
        <q-btn round color="primary" icon="add" size="lg" class="add-btn" @click="addMember" />
      </div>
    </div>

    <!-- Title Section -->
    <div class="text-h6 text-bold q-mb-sm" style="color: #2d3a4a">Title</div>
    <div class="row items-center q-mb-lg">
      <div class="col">
        <q-input
          v-model="title"
          outlined
          dense
          class="title-input"
          placeholder="Enter thesis title"
        />
      </div>
      <div class="col-auto">
        <q-btn
          color="primary"
          class="upload-btn"
          label="Upload File"
          icon="cloud_upload"
          @click="triggerFileInput"
        />
        <input type="file" ref="fileInput" class="hidden" @change="onFileChange" />
      </div>
    </div>

    <!-- Description Section -->
    <div class="text-h6 text-bold q-mb-sm" style="color: #2d3a4a">Description</div>
    <q-input
      v-model="description"
      type="textarea"
      outlined
      autogrow
      class="desc-input"
      placeholder="Enter thesis description"
    />

    <!-- Submit Section -->
    <div class="q-mt-lg">
      <q-btn color="primary" class="submit-btn" label="Submit Thesis" @click="submitThesis" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const fileInput = ref(null)
const selectedFile = ref(null)

const groupMembers = ref([
  {
    name: 'Abdul GGs',
    year: '2021-2022',
    id: '202356735',
    department: 'Computer Science',
  },
  {
    name: 'Mjolnir Rizz',
    year: '2021-2022',
    id: '202356735',
    department: 'Computer Science',
  },
])

const title = ref('CICS Thesis Archive Frontend')
const description = ref(
  `Hello World! This is a sample description for the thesis. It can be as long as you want it to be, and it will automatically grow as you type.`,
)

function addMember() {
  groupMembers.value.push({
    name: '',
    year: '',
    id: '',
    department: '',
  })
}

function removeMember(index) {
  if (groupMembers.value.length > 1) {
    groupMembers.value.splice(index, 1)
  }
}

function triggerFileInput() {
  fileInput.value.click()
}

function onFileChange(event) {
  selectedFile.value = event.target.files[0]
  uploadFile()
}

async function uploadFile() {
  if (!selectedFile.value) {
    alert('Please select a file to upload.')
    return
  }
  const formData = new FormData()
  formData.append('file', selectedFile.value)

  try {
    await axios.post('http://localhost:8000/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    alert('Upload success!')
    // handle response as needed
  } catch (err) {
    alert('Upload failed!')
    console.error(err)
  }
}

async function submitThesis() {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('description', description.value)
  formData.append('groupMembers', JSON.stringify(groupMembers.value))
  if (selectedFile.value) {
    formData.append('file', selectedFile.value)
  }

  try {
    await axios.post('http://localhost:8000/thesis', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    alert('Thesis submitted successfully!')
  } catch (err) {
    alert('Submission failed!')
    console.error(err)
  }
}
</script>

<style scoped>
.member-card {
  border-radius: 16px;
  background: #fff;
}
.add-btn {
  background: #e6edfa !important;
  color: #1976d2 !important;
  box-shadow: 0 2px 8px #1976d233;
}
.title-input {
  border-radius: 16px;
  background: #fff;
  font-weight: bold;
  font-size: 1.1rem;
}
.upload-btn {
  border-radius: 24px;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 4px 12px #1976d233;
  padding: 0 24px;
}
.desc-input {
  border-radius: 16px;
  background: #fff;
  font-size: 1rem;
}
.hidden {
  display: none;
}
</style>
