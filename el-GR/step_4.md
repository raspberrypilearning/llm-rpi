<iframe width="560" height="315" src="https://www.youtube.com/embed/xx0VQ0RJc8A?si=MeRR763nVpucx5d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Χρήση του WebUI

Το WebUI λειτουργεί όπως οποιαδήποτε άλλη διεπαφή chatbot. Μπορείς να πληκτρολογήσεις τις προτροπές σου και να δεις τις απαντήσεις που παράγονται από το μοντέλο.

![Ένα στιγμιότυπο οθόνης μιας διεπαφής ΤΝ που εμφανίζει έναν καθαρό, μινιμαλιστικό σχεδιασμό. Το κείμενο «Hello, MrC» παρουσιάζεται εμφανώς στο κέντρο. Παρακάτω, υπάρχει μια γραμμή αναζήτησης με την ετικέτα "How can I help you today?" με ένα εικονίδιο μικροφώνου και ήχου στα δεξιά. Προτεινόμενες προτροπές περιλαμβάνουν: "Tell me a fun fact about the Roman Empire," "Show me a code snippet of a website's sticky header," και "Give me ideas for what to do with my kids' art." Στην αριστερή πλευρά, υπάρχει ένα μενού με επιλογές για "Workspace," "Search," and "Chats." Ένα κυκλικό εικονίδιο προφίλ με την ένδειξη "M" βρίσκεται στην επάνω δεξιά γωνία.](images/webUI.png)

### Εγκατάσταση Docker και WebUI

--- task ---

Εγκατάστησε το Docker εισάγοντας την ακόλουθη εντολή στο τερματικό:

```bash
sudo apt install docker.io
```

Περίμενε να εγκατασταθεί το Docker. Θα καταλάβεις ότι η εγκατάσταση έχει ολοκληρωθεί όταν εμφανιστεί το σύμβολο προτροπής του τερματικού.

--- /task ---

--- task ---

Εγκατάστησε το WebUI αντιγράφοντας και επικολλώντας την ακόλουθη εντολή στο τερματικό:

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Περίμενε να εγκατασταθεί το WebUI. Θα καταλάβεις ότι η εγκατάσταση έχει ολοκληρωθεί όταν εμφανιστεί το σύμβολο προτροπής του τερματικού.

--- /task ---

--- task ---

Απόκτησε πρόσβαση στη διεπαφή WebUI μεταβαίνοντας στη διεύθυνση `http://localhost:3000/` στο πρόγραμμα περιήγησής σου στο διαδίκτυο.

![Μια καρτέλα με τίτλο "Open WebUI" εμφανίζει το URL "localhost:3000" στη γραμμή διευθύνσεων.](images/localhostURL.png)

--- /task ---
