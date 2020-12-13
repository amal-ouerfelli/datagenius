import http from "../http-commun";

class TutorialDataService {
 
  create(data) {
    return http.post("/api/panier", data);
  }
}
export default new TutorialDataService();